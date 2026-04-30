# 🚲 Bike Sharing Analytics Dashboard

Proyek ini merupakan submission akhir dari kelas **"Belajar Fundamental Analisis Data"** pada program Coding Camp 2026 by Dicoding yang berfokus pada eksplorasi, analisis, dan visualisasi data penyewaan sepeda (Bike Sharing). Proyek mencakup seluruh tahapan analisis data mulai dari *Data Wrangling*, *Exploratory Data Analysis* (EDA), hingga pembuatan dashboard interaktif menggunakan **Streamlit**.

---

## 📊 Ringkasan Proyek

Tujuan utama proyek ini adalah mengungkap pola dan insight dari data penyewaan sepeda, seperti:
*   **Pengaruh Kondisi Cuaca:** Mengetahui bagaimana elemen atmosfer memengaruhi minat penyewa.
*   **Pola Penggunaan Berdasarkan Waktu:** Membedakan perilaku pengguna pada hari kerja vs akhir pekan.
*   **Karakteristik & Segmentasi:** Memahami perbedaan profil antara pengguna kasual dan pengguna terdaftar.

---

## ❓ Pertanyaan Bisnis

### 🌦️ Analisis Cuaca
*   Bagaimana pengaruh kondisi cuaca (weathershit) terhadap rata-rata jumlah penyewaan sepeda per jam?
### ⏰ Analisis Waktu
*   Bagaimana pengaruh kondisi cuaca (weathershit) terhadap rata-rata jumlah penyewaan sepeda per jam?

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
│   ├── dashboard.py       # Dashboard utama Streamlit
│   ├── all_data.csv       # Dataset hasil cleaning
│   └── logo.png           # Logo dashboard
│
├── data/
│   ├── day.csv            # Data mentah harian
│   └── hour.csv           # Data mentah per jam
│
├── notebook.ipynb         # Proses Wranling, EDA & insight
├── requirements.txt       # Library yang dibutuhkan
├── url.txt                # Link dashboard publik
└── README.md              # Dokumentasi proyek
```

### Cara Cepat Jalankan (Windows)
```bash
git clone [https://github.com/username/proyek-analisis-data.git](https://github.com/username/proyek-analisis-data.git)
cd proyek-analisis-data
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
