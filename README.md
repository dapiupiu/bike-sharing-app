# 🚲 Bike Sharing Analytics — Bike Sharing Analytics Dashboard

Ringkasan singkat: proyek ini adalah analisis dan visualisasi data penyewaan sepeda yang menyajikan insight waktu-nyata melalui dashboard interaktif berbasis Streamlit. Cocok untuk eksplorasi pola penggunaan, pengaruh cuaca, dan segmentasi pengguna.

Demo publik: https://bike-sharing-app-gyagtguyba67ulc3jz6vpw.streamlit.app/

## ✨ Kenapa proyek ini menarik?
- Cepat: buka dashboard interaktif, filter, dan langsung lihat insight.
- Informatif: kombinasi EDA, visualisasi, dan metrik inti membuat cerita data mudah dicerna.
- Reproducible: semua notebook dan dataset disertakan agar analisis dapat direplikasi.

## 🎯 Highlight (Apa yang bisa Anda lakukan di dashboard)
- Melihat metrik ringkasan: total rides, pengguna terdaftar vs kasual.
- Eksplorasi pola per jam / per hari: bandingkan hari kerja vs akhir pekan.
- Analisis pengaruh cuaca terhadap jumlah peminjaman.
- Deep-dive: korelasi fitur, distribusi musiman, dan insight tambahan dari notebook.

## 🗂️ Struktur utama proyek
Berisi file dan folder penting yang akan Anda gunakan:
- `dashboard/dashboard.py`: aplikasi Streamlit untuk eksplorasi interaktif.
- `dashboard/all_data.csv`: dataset hasil proses pembersihan (digunakan dashboard).
- `data/day.csv` dan `data/hour.csv`: dataset mentah (harian & per jam) untuk EDA.
- `notebook.ipynb`: proses data-wrangling, EDA, visualisasi, dan insight lengkap.
- `requirements.txt`: daftar dependensi Python.
- `url.txt`: link deployment Streamlit.

## 🚀 Jalankan lokal (cara cepat)
1. Buat virtual environment dan aktifkan:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # macOS / Linux
```

2. Instal dependensi dan jalankan dashboard:

```bash
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
```

3. Jalankan dashboard sesuai dengan alamat localhost.

## 📌 Tip interaktif
- Gunakan slider waktu dan dropdown kondisi cuaca di dashboard untuk melihat perubahan metrik secara real-time.
- Buka `notebook.ipynb` untuk melihat langkah-langkah pembersihan dan visualisasi yang menghasilkan dataset `dashboard/all_data.csv`.

## 🛠️ Untuk kontributor
- Perbarui notebook atau tambahkan notebook baru untuk eksperimen.
- Jika menambah dependensi, perbarui `requirements.txt`.
- Buat PR dengan deskripsi perubahan dan contoh output.

---