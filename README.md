Tugas Kelompok
https://docs.google.com/document/d/1rc4A9wh-m_TwFmsjlzDSrOlA4LuLH2_dJGCpBjEAv4g/edit?tab=t.0




Analisis 1
Pada list biasa, [5000, 7000, 3000] * 0.9 akan error (TypeError) karena operator * pada
list berfungsi untuk menduplikasi isi (hanya terima bilangan bulat), bukan menghitung matematika.
Sebaliknya, pada NumPy Array operasi ini berhasil ([4500., 6300., 2700.])
karena NumPy otomatis mengalikan angka 0.9 ke setiap elemennya (vectorized operation).

Analisis 2
 Kolom yang memiliki data kosong adalah menu (indeks ke-4) dan terjual (indeks ke-2).
#Risikonya jika langsung dianalisis tanpa dibersihkan adalah perhitungan matematika menjadi tidak akurat
(misalnya total pendapatan dari harga * terjual akan menghasilkan nilai kosong/ NaN), serta informasi menu
menjadi tidak jelas karena ada data transaksi yang tidak diketahui nama barangnya.

Analisis 3
Kolom yang jumlah non-null-nya lebih sedikit adalah
kolom menu dan terjual (berdasarkan data kantin sebelumnya).
Artinya, kedua kolom tersebut memiliki nilai kosong (missing values / NaN),
sehingga ada beberapa baris data yang belum terisi secara lengkap dan perlu dibersihkan sebelum dianalisis lebih lanjut.

Analisis 4
terjual diisi 0 (fillna): Karena data angka bernilai kosong logis diasumsikan belum ada penjualan (0 unit), sehingga datanya masih bisa dihitung secara matematis tanpa merusak analisis.
menu dihapus (dropna): Karena menu adalah identitas utama item (kategori). Jika nama menunya tidak ada, data angka di baris tersebut menjadi tidak bermakna/tidak dapat diidentifikasi
milik produk mana.

 Analisis 5
Jumlah baris: Berkurang dari 5 baris menjadi 3 baris (karena ada 1 data ganda 'Es Teh' yang dihapus dan 1 baris ber-menu kosong yang sudah dibuang di latihan sebelumnya).
Pentingnya tipe data (dtypes): Memastikan tipe data benar sangat krusial agar fungsi analisis dan operasi matematika bekerja tepat.
Jika harga bertipe string (teks), operasi seperti penjumlahan atau perkalian akan gagal atau salah (misalnya teks "4000" + "4000" menjadi "40004000", bukan 8000).

Analisi 6
Menu pendapatan tertinggi: Nasi Goreng (dengan total pendapatan Rp276.000, hasil dari 12.000 × 23).
Manfaat pengambilan keputusan: Informasi ini membantu pengelola kantin untuk memprioritaskan stok bahan baku menu paling menguntungkan agar tidak kehabisan,
serta menentukan strategi promosi atau evaluasi harga untuk menu-menu lain yang peminatnya masih rendah.
