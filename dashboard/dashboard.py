import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- SETUP PAGE & LOAD DATA ---
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/all_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Buat kolom 'day_type' jika belum ada, berdasarkan 'holiday' dan 'workingday'
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

# --- SIDEBAR WITH FILTERS ---
with st.sidebar:
    st.image("dashboard/logo.png")
    st.title("Bike Sharing Filter")
    
    # Filter Rentang Waktu
    min_date = all_data_df["dteday"].min()
    max_date = all_data_df["dteday"].max()
    
    try:
        date_range = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
        if len(date_range) == 2:
            start_date, end_date = date_range
        else:
            start_date = end_date = date_range[0]
    except Exception:
        start_date = end_date = min_date

    # Filter Musim (Multiselect)
    all_seasons = all_data_df['season'].unique()
    selected_seasons = st.multiselect(
        "Pilih Musim:",
        options=all_seasons,
        default=all_seasons
    )

# Terapkan filter pada DataFrame utama
main_df = all_data_df[
    (all_data_df["dteday"] >= pd.to_datetime(start_date)) & 
    (all_data_df["dteday"] <= pd.to_datetime(end_date)) &
    (all_data_df["season"].isin(selected_seasons))
]

# --- MAIN PAGE HEADER & METRICS ---
st.header('Bike Sharing Analytics Dashboard 🚲')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sharing", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Total Registered", value=f"{main_df.registered.sum():,}")
with col3:
    st.metric("Total Casual", value=f"{main_df.casual.sum():,}")

st.divider()

# --- TABS SYSTEM ---
tab1, tab2 = st.tabs(["Main Trends", "Deep Dive Analysis"])

# TAB 1: Visualisasi Pertanyaan Bisnis Utama
with tab1:
    st.subheader("Business Questions Insights")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.write("### Performance by Weather Condition")
        fig_weather, ax_weather = plt.subplots(figsize=(10, 8))
        sns.barplot(x="weathersit", y="cnt", data=main_df, palette="viridis", ax=ax_weather, errorbar=None)
        ax_weather.set_ylabel("Rata-rata Penyewaan")
        st.pyplot(fig_weather)
        
        with st.expander("Lihat Analisis Cuaca"):
            st.write("""
                * **Dominasi Cuaca Cerah:** Kondisi **Clear/Cerah** secara konsisten menghasilkan penyewaan tertinggi.
                * **Dampak Hujan/Salju:** Terjadi penurunan drastis saat kondisi beralih ke hujan atau salju ringan.
                * **Rekomendasi:** Siapkan strategi operasional khusus saat musim hujan tiba.
            """)

    with col_right:
        st.write("### User Segmentation: Casual vs Registered")
        user_data = pd.DataFrame({
            'User Type': ['Casual', 'Registered'],
            'Total': [main_df['casual'].sum(), main_df['registered'].sum()]
        })
        
        fig_user, ax_user = plt.subplots(figsize=(10, 8))
        ax_user.pie(
            user_data['Total'], 
            labels=user_data['User Type'], 
            autopct='%1.1f%%', 
            colors=['#72BCD4', '#2ca02c'],
            startangle=90,
            wedgeprops={'edgecolor': 'white'}
        )
        st.pyplot(fig_user)

        with st.expander("Lihat Analisis Segmentasi"):
            st.write("""
                * **Pilar Bisnis:** Pengguna **Registered** berkontribusi lebih dari **80%**.
                * **Peluang Casual:** Pengguna kasual cenderung memuncak pada hari libur.
                * **Rekomendasi:** Fokus pada retensi member sambil menarik pengguna kasual di akhir pekan.
            """)

    st.write("### Hourly Patterns by Day Type")
    fig_hour, ax_hour = plt.subplots(figsize=(16, 8))
    sns.lineplot(
        data=main_df, 
        x="hr", 
        y="cnt", 
        hue="day_type", 
        marker="o", 
        ax=ax_hour,
        palette={"Working Day": "#1f77b4", "Weekend": "#ff7f0e", "Holiday": "#d62728"}
    )
    ax_hour.set_xticks(range(0, 24))
    ax_hour.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig_hour)

    with st.expander("Lihat Analisis Pola Waktu"):
        st.write("""
            * **Pola M-Shape (Hari Kerja):** Lonjakan pada pukul **08:00** dan **17:00** (jam komuter).
            * **Pola Bell-Curve (Akhir Pekan):** Puncak bergeser ke pukul **12:00 - 14:00** (rekreasi).
        """)

# TAB 2: Analisis Statistik Mendalam
with tab2:
    st.subheader("Advanced Data Exploration")
    
    # Heatmap Korelasi & Feature Importance
    col_corr, col_feat = st.columns(2)
    
    with col_corr:
        st.write("### Correlation Matrix")
        corr_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
        correlation_matrix = main_df[corr_cols].corr()
        
        fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax_corr)
        st.pyplot(fig_corr)
        
    with col_feat:
        st.write("### Feature Importance (to Count)")
        # Menghitung korelasi absolut terhadap 'cnt'
        importance = main_df[corr_cols].corr()['cnt'].sort_values(ascending=False).drop('cnt')
        
        fig_feat, ax_feat = plt.subplots(figsize=(10, 8))
        importance.plot(kind='barh', color='#72BCD4', ax=ax_feat)
        ax_feat.set_xlabel("Skor Korelasi")
        st.pyplot(fig_feat)

    with st.expander("Lihat Insight Korelasi"):
        st.write("""
            * **Suhu (Temp):** Memiliki korelasi positif terkuat dengan jumlah penyewaan.
            * **Kelembapan (Hum):** Memiliki korelasi negatif, menandakan minat menurun saat udara terlalu lembap/mendung.
        """)

    # Boxplot & Outlier Analysis
    st.write("### Seasonal Distribution & Outliers")
    fig_box, ax_box = plt.subplots(figsize=(16, 8))
    sns.boxplot(x="season", y="cnt", data=main_df, palette="rocket", ax=ax_box)
    ax_box.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig_box)
    
    with st.expander("Lihat Analisis Outlier"):
        st.write("""
            * **Variabilitas Musiman:** Musim gugur (*Fall*) cenderung memiliki rata-rata penyewaan tertinggi.
            * **Karakteristik Outlier:** Titik-titik di atas kumis boxplot menunjukkan lonjakan permintaan ekstrem yang valid, sering terjadi pada jam sibuk atau cuaca ideal.
            * **Integritas Data:** Nilai ekstrem ini tidak dihapus karena merupakan representasi nyata dari *peak demand*.
        """)

st.caption(f'Copyright (c) Kaka Davi Dharmawan {pd.Timestamp.now().year}')