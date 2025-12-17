# P14-Verifikasi-Kode-Debugging-dan-Unit-Testing-Sederhana
Pertemuan 14: Verifikasi Kode: Debugging dan Unit Testing Sederhana

# Deskripsi
Proyek ini berisi program kalkulator yang menghitung diskon dengan logika perhitungan diskon, Hasil diskon diuji dengan *unittest* untuk menguji fleksibilitas program dalam mengatasi bug atau *debugging*. Permasalahan yang berada pada program ini antara lain: Bug 1000% dan Bug PPN 10%.

# Struktur File
- `DEBUG_REPORT.md` : Laporan yang berisi Debug Log
- `diskon_service.py` : Program utama untuk perhitungan diskon
- `test_diskon_advanced.py` : Program penngujian unittest lanjutan untuk menghitung nilai float dan edge (nilai 0)
- `test_diskon.py` : Program pengujian unittest untuk memastikan nilai pada diskon 10%, Diskon 0% yang tidak mengubah harga, Diskon 100% yang menghasilkan 0, dan Diskon negatif yang tidak mempengaruhi harga
