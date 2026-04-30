# 🚲 Bike Sharing Analytics Dashboard

Proyek ini merupakan tugas akhir dari program belajar **Data Analytics** yang berfokus pada eksplorasi, analisis, dan visualisasi data penyewaan sepeda. Proyek mencakup seluruh tahapan analisis data mulai dari *Data Wrangling*, *Exploratory Data Analysis* (EDA), hingga pembuatan dashboard interaktif menggunakan **Streamlit**.

---

## 📊 Ringkasan Proyek

Tujuan utama proyek ini adalah mengungkap pola dan insight dari data penyewaan sepeda, seperti:
*   **Pengaruh Kondisi Cuaca:** Mengetahui bagaimana elemen atmosfer memengaruhi minat penyewa.
*   **Pola Penggunaan Berdasarkan Waktu:** Membedakan perilaku pengguna pada hari kerja vs akhir pekan.
*   **Karakteristik & Segmentasi:** Memahami perbedaan profil antara pengguna kasual dan pengguna terdaftar.

---

## ❓ Pertanyaan Bisnis

### 🌦️ Analisis Cuaca
*   Bagaimana kondisi cuaca memengaruhi rata-rata jumlah penyewaan sepeda?

### ⏰ Analisis Waktu
*   Di jam berapa terjadi puncak penyewaan sepeda pada:
    *   Hari kerja?
    *   Hari libur / akhir pekan?

---

## 🚀 Fitur Utama Dashboard

*   **📌 Metrics Summary:** Menampilkan total penyewaan, pengguna terdaftar, dan pengguna kasual secara dinamis.
*   **🌦️ Weather Performance:** Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan.
*   **⏰ Hourly Patterns:** Perbandingan pola penggunaan antara komuter (hari kerja) dan rekreasi (akhir pekan).
*   **👥 User Segmentation:** Analisis proporsi antara pengguna *Casual* dan *Registered*.
*   **🔍 Deep Dive Analysis:** Analisis lanjutan meliputi matriks korelasi, *feature importance*, dan distribusi musiman (*boxplot*).

---

## 🛠️ Struktur Folder
```text
.
├── dashboard/
│   ├── dashboard.py       # Aplikasi utama Streamlit
│   ├── all_data.csv       # Dataset hasil cleaning
│   └── logo.png           # Logo dashboard
│
├── data/
│   ├── day.csv            # Data mentah harian
│   └── hour.csv           # Data mentah per jam
│
├── notebook.ipynb         # Proses EDA & analisis data
├── requirements.txt       # Library yang dibutuhkan
├── url.txt                # Link dashboard publik
└── README.md              # Dokumentasi proyek