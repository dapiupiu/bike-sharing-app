import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/all_data.csv")

    # Convert datetime
    df['dteday'] = pd.to_datetime(df['dteday'])

    # Membuat kolom day_type jika belum ada
    if 'day_type' not in df.columns:

        def get_day_type(row):
            if row['holiday'] == 1 or row['holiday'] == 'Holiday':
                return 'Holiday'

            elif row['workingday'] == 1 or row['workingday'] == 'Working Day':
                return 'Working Day'

            else:
                return 'Weekend'

        df['day_type'] = df.apply(get_day_type, axis=1)

    return df


all_data_df = load_data()

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.image("dashboard/logo.png")

    st.title("Bike Sharing Filter")

    # =========================
    # DATE FILTER
    # =========================
    min_date = all_data_df["dteday"].min()
    max_date = all_data_df["dteday"].max()

    try:

        date_range = st.date_input(
            label="Rentang Waktu",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date)
        )

        # Jika user memilih range tanggal
        if isinstance(date_range, tuple) and len(date_range) == 2:
            start_date, end_date = date_range

        # Jika user memilih satu tanggal
        else:
            start_date = end_date = date_range

    except Exception:
        start_date = min_date
        end_date = max_date

    # =========================
    # SEASON FILTER
    # =========================
    all_seasons = sorted(all_data_df['season'].unique().tolist())

    options = ["All"] + all_seasons

    selected_seasons = st.multiselect(
        "Pilih Musim:",
        options=options,
        default=["All"]
    )

# =========================
# MAIN FILTERING
# =========================

# Filter berdasarkan tanggal
main_df = all_data_df[
    (all_data_df["dteday"] >= pd.to_datetime(start_date)) &
    (all_data_df["dteday"] <= pd.to_datetime(end_date))
]

# Filter musim
if "All" not in selected_seasons:
    main_df = main_df[
        main_df["season"].isin(selected_seasons)
    ]

# =========================
# VALIDASI DATA
# =========================
if main_df.empty:
    st.warning("Tidak ada data yang sesuai filter.")
    st.stop()

# =========================
# HEADER
# =========================
st.header("Bike Sharing Analytics Dashboard 🚲")

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sharing",
        value=f"{main_df['cnt'].sum():,}"
    )

with col2:
    st.metric(
        "Total Registered",
        value=f"{main_df['registered'].sum():,}"
    )

with col3:
    st.metric(
        "Total Casual",
        value=f"{main_df['casual'].sum():,}"
    )

st.divider()

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs([
    "Main Trends",
    "Deep Dive Analysis"
])

# =========================================================
# TAB 1
# =========================================================
with tab1:

    st.subheader("Business Questions Insights")

    col_left, col_right = st.columns(2)

    # =========================
    # WEATHER ANALYSIS
    # =========================
    with col_left:

        st.write("### Performance by Weather Condition")

        fig_weather, ax_weather = plt.subplots(figsize=(10, 8))

        sns.barplot(
            x="weathersit",
            y="cnt",
            data=main_df,
            palette="viridis",
            errorbar=None,
            ax=ax_weather
        )

        ax_weather.set_ylabel("Rata-rata Penyewaan")

        st.pyplot(fig_weather)

        with st.expander("Lihat Analisis Cuaca"):

            st.write("""
            * **Dominasi Cuaca Cerah:** Kondisi cerah menghasilkan penyewaan tertinggi.
            * **Dampak Hujan/Salju:** Penyewaan menurun drastis saat hujan.
            * **Rekomendasi:** Siapkan strategi khusus pada cuaca hujan.
            """)

    # =========================
    # USER SEGMENTATION
    # =========================
    with col_right:

        st.write("### User Segmentation: Casual vs Registered")

        user_data = pd.DataFrame({
            'User Type': ['Casual', 'Registered'],
            'Total': [
                main_df['casual'].sum(),
                main_df['registered'].sum()
            ]
        })

        # Menghindari NaN
        user_data['Total'] = user_data['Total'].fillna(0)

        if user_data['Total'].sum() > 0:

            fig_user, ax_user = plt.subplots(figsize=(10, 8))

            ax_user.pie(
                user_data['Total'],
                labels=user_data['User Type'].astype(str).tolist(),
                autopct='%1.1f%%',
                colors=['#72BCD4', '#2ca02c'],
                startangle=90,
                wedgeprops={'edgecolor': 'white'}
            )

            st.pyplot(fig_user)

        else:
            st.warning("Data segmentasi user kosong.")

        with st.expander("Lihat Analisis Segmentasi"):

            st.write("""
            * **Pengguna Registered** mendominasi total penyewaan.
            * **Pengguna Casual** meningkat pada akhir pekan/libur.
            * **Strategi:** Fokus retensi member dan promosi akhir pekan.
            """)

    # =========================
    # HOURLY PATTERN
    # =========================
    st.write("### Hourly Patterns by Day Type")

    fig_hour, ax_hour = plt.subplots(figsize=(16, 8))

    sns.lineplot(
        data=main_df,
        x="hr",
        y="cnt",
        hue="day_type",
        marker="o",
        palette={
            "Working Day": "#1f77b4",
            "Weekend": "#ff7f0e",
            "Holiday": "#d62728"
        },
        ax=ax_hour
    )

    ax_hour.set_xticks(range(0, 24))
    ax_hour.set_ylabel("Rata-rata Penyewaan")

    st.pyplot(fig_hour)

    with st.expander("Lihat Analisis Pola Waktu"):

        st.write("""
        * Hari kerja memiliki pola komuter pagi dan sore.
        * Akhir pekan memiliki puncak aktivitas siang hari.
        """)

# =========================================================
# TAB 2
# =========================================================
with tab2:

    st.subheader("Advanced Data Exploration")

    corr_cols = [
        'temp',
        'atemp',
        'hum',
        'windspeed',
        'casual',
        'registered',
        'cnt'
    ]

    col_corr, col_feat = st.columns(2)

    # =========================
    # CORRELATION MATRIX
    # =========================
    with col_corr:

        st.write("### Correlation Matrix")

        correlation_matrix = main_df[corr_cols].corr()

        fig_corr, ax_corr = plt.subplots(figsize=(10, 8))

        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            ax=ax_corr
        )

        st.pyplot(fig_corr)

    # =========================
    # FEATURE IMPORTANCE
    # =========================
    with col_feat:

        st.write("### Feature Importance (to Count)")

        importance = (
            main_df[corr_cols]
            .corr()['cnt']
            .sort_values(ascending=False)
            .drop('cnt')
        )

        fig_feat, ax_feat = plt.subplots(figsize=(10, 8))

        importance.plot(
            kind='barh',
            color='#72BCD4',
            ax=ax_feat
        )

        ax_feat.set_xlabel("Skor Korelasi")

        st.pyplot(fig_feat)

    with st.expander("Lihat Insight Korelasi"):

        st.write("""
        * Suhu memiliki korelasi positif kuat terhadap jumlah penyewaan.
        * Kelembapan tinggi cenderung menurunkan minat penyewaan.
        """)

    # =========================
    # BOXPLOT
    # =========================
    st.write("### Seasonal Distribution & Outliers")

    fig_box, ax_box = plt.subplots(figsize=(16, 8))

    sns.boxplot(
        x="season",
        y="cnt",
        data=main_df,
        palette="rocket",
        ax=ax_box
    )

    ax_box.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig_box)

    with st.expander("Lihat Analisis Outlier"):

        st.write("""
        * Musim tertentu menunjukkan rata-rata penyewaan lebih tinggi.
        * Outlier menunjukkan peak demand yang valid.
        * Nilai ekstrem dipertahankan karena mencerminkan kondisi nyata.
        """)

# =========================
# FOOTER
# =========================
st.caption(
    f"Copyright (c) Kaka Davi Dharmawan {pd.Timestamp.now().year}"
)