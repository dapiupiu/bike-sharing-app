# Bike Sharing Analytics Dashboard

Proyek ini merupakan salah satu proyek analisis data yang berfokus pada eksplorasi, analisis, dan visualisasi data penyewaan sepeda (Bike Sharing). Proyek mencakup seluruh tahapan analisis data mulai dari *Data Wrangling*, *Exploratory Data Analysis* (EDA), hingga pembuatan dashboard interaktif menggunakan **Streamlit**.

---

**Link Dashboard: https://bike-sharing-app-kakadavidharmawan.streamlit.app/**

---

## Temuan Utama

- **Cuaca:** rata-rata penyewaan 204,9/jam saat cerah vs 112,8/jam saat hujan/salju ringan (turun 44,9%); cuaca berkabut turun 14,5%.
- **Pola jam:** hari kerja punya dua puncak (08:00 ≈ 478/jam dan 17:00 ≈ 526/jam), sedangkan akhir pekan/libur punya satu puncak pukul 13:00 (≈ 373/jam).
- **Musim:** musim panas (Jun–Sep) tertinggi dengan rata-rata 236/jam, sekitar 2,1× musim dingin (111,5/jam).
- **Pengguna:** pengguna terdaftar menyumbang 81,2% dari total penyewaan.
- **Faktor lingkungan:** suhu berkorelasi positif sedang dengan penyewaan (r = 0,40), kelembapan negatif (r = −0,33).

---

## Ringkasan Proyek

Tujuan utama proyek ini adalah mengungkap pola dan insight dari data penyewaan sepeda, seperti:
*   **Pengaruh Kondisi Cuaca:** Mengetahui bagaimana elemen atmosfer memengaruhi minat penyewa.
*   **Pola Penggunaan Berdasarkan Waktu:** Membedakan perilaku pengguna pada hari kerja vs akhir pekan.
*   **Karakteristik & Segmentasi:** Memahami perbedaan profil antara pengguna kasual dan pengguna terdaftar.

---

## Pertanyaan Bisnis

### Analisis Cuaca
*   Bagaimana pengaruh kondisi cuaca (weathersit) terhadap rata-rata jumlah penyewaan sepeda per jam?
### Analisis Waktu
*   Di jam berapa terjadi puncak penyewaan sepeda pada hari kerja (workingday) dibandingkan dengan hari libur (holiday)?

---

## Fitur Utama Dashboard

*   **Metrics Summary:** Menampilkan total penyewaan, pengguna terdaftar, dan pengguna kasual secara dinamis.
*   **Weather Performance:** Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan.
*   **Hourly Patterns:** Perbandingan pola penggunaan antara komuter (hari kerja) dan rekreasi (akhir pekan).
*   **User Segmentation:** Analisis proporsi antara pengguna *Casual* dan *Registered*.
*   **Deep Dive Analysis:** Analisis lanjutan meliputi matriks korelasi, korelasi terhadap jumlah penyewaan, dan distribusi musiman (*boxplot*).

---

## Struktur Folder
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
├── notebook.ipynb         # Proses Wrangling, EDA & insight
├── requirements.txt       # Library yang dibutuhkan
├── url.txt                # Link dashboard publik
└── README.md              # Dokumentasi proyek
```

### Cara Cepat Menjalankan Proyek (Windows)
```bash
git clone https://github.com/dapiupiu/bike-sharing-app.git
cd bike-sharing-app
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # macOS / Linux
```

Instal dependensi dan jalankan dashboard:

```bash
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

Jalankan dashboard sesuai dengan alamat localhost.

## Tip interaktif
- Gunakan filter Rentang Waktu dan Pilih Musim di sidebar untuk melihat perubahan metrik secara dinamis.
- Buka `notebook.ipynb` untuk melihat langkah-langkah pembersihan dan visualisasi yang menghasilkan dataset `dashboard/all_data.csv`.

## Untuk kontributor
- Perbarui notebook atau tambahkan notebook baru untuk eksperimen.
- Jika menambah dependensi, perbarui `requirements.txt`.
- Buat PR dengan deskripsi perubahan dan contoh output.

---
