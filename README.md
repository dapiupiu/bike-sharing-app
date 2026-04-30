# 🚲 Bike Sharing Analytics Dashboard

Proyek ini merupakan tugas akhir dari program belajar **Data Analytics** yang berfokus pada eksplorasi, analisis, dan visualisasi data penyewaan sepeda. Proyek mencakup seluruh tahapan analisis data mulai dari **Data Wrangling**, **Exploratory Data Analysis (EDA)**, hingga pembuatan **dashboard interaktif menggunakan Streamlit**.

---

## 📊 Ringkasan Proyek

Tujuan utama proyek ini adalah mengungkap pola dan insight dari data penyewaan sepeda, seperti:

- Pengaruh kondisi cuaca terhadap jumlah penyewaan
- Pola penggunaan berdasarkan waktu (hari kerja vs akhir pekan)
- Karakteristik dan segmentasi pengguna

---

## ❓ Pertanyaan Bisnis

### 🌦️ Analisis Cuaca
Bagaimana kondisi cuaca memengaruhi rata-rata jumlah penyewaan sepeda?

### ⏰ Analisis Waktu
Di jam berapa terjadi puncak penyewaan sepeda pada:
- Hari kerja
- Hari libur / akhir pekan

---

## 🚀 Fitur Utama Dashboard

- **📌 Metrics Summary**  
  Menampilkan total penyewaan, pengguna terdaftar, dan pengguna kasual secara dinamis berdasarkan filter.

- **🌦️ Weather Performance**  
  Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan.

- **⏰ Hourly Patterns**  
  Perbandingan pola penggunaan:
  - Komuter (hari kerja)
  - Rekreasi (akhir pekan)

- **👥 User Segmentation**  
  Analisis proporsi pengguna:
  - Casual
  - Registered

- **🔍 Deep Dive Analysis**  
  Analisis lanjutan meliputi:
  - Matriks korelasi
  - Feature importance
  - Distribusi musiman (boxplot)

---

## 🛠️ Struktur Folder
├── dashboard/
│ ├── dashboard.py # Aplikasi utama Streamlit
│ ├── all_data.csv # Dataset hasil cleaning
│ └── logo.png # Logo dashboard
│
├── data/
│ ├── day.csv # Data mentah harian
│ └── hour.csv # Data mentah per jam
│
├── notebook.ipynb # Proses EDA & analisis data
├── requirements.txt # Library yang dibutuhkan
├── url.txt # Link dashboard publik
└── README.md # Dokumentasi proyek


---

## 💻 Cara Menjalankan Dashboard

### 1. Clone Repository
```bash
git clone https://github.com/username/proyek-analisis-data.git
cd proyek-analisis-data
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
streamlit run dashboard/dashboard.py