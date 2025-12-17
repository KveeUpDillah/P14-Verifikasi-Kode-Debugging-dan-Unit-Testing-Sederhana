# Langkah - Langkah pdb
1. Mengecek variabel dari operasi pertama yaitu "jumlah_diskon" yaitu "harga_awal" dan "persentase_diskon". 
2. Kedua variabel telah memiliki perhitungan yang benar untuk mendapatkan 10% yaitu 1000 * 10 / 100. dan menghasilkan 10%.
3. Mengecek variabel operasi kedua yaitu "harga_akhir" yaitu "harga_awal" dan "jumlah_diskon". 
4. Kesalahan terdapat disini karena operasi melakukan penambahan 10% yang kedua, sehingga terajadi bug yang seharusnya diskon mengurangi harga sebanyak 100 malah mengurangi harga sebanyak 10 menjadikan PPN dihitung 2x yaitu 10% * 10%.
