import numpy as np
import pandas as pd
#Latihan 1: Operasi Dasar NumPy Array
harga = np.array([5000, 7000, 3000, 12000, 4500])
print('Rata-rata harga:', harga.mean())
print('Harga tertinggi:', harga.max())
print('Harga setelah diskon 10%:', harga * 0.9)
#Analisis
harga_array = np.array([5000, 7000, 3000])
print(harga_array * 0.9)

# Menggunakan List Biasa (Error)
harga_list = [5000, 7000, 3000]
print(harga_list * 0.9)  
#Pada list biasa, [5000, 7000, 3000] * 0.9 akan error (TypeError) karena operator * pada
#  list berfungsi untuk menduplikasi isi (hanya terima bilangan bulat), bukan menghitung matematika.
#  Sebaliknya, pada NumPy Array operasi ini berhasil ([4500., 6300., 2700.])
#  karena NumPy otomatis mengalikan angka 0.9 ke setiap elemennya (vectorized operation).

#Latihan 2: Membuat Series & DataFrame
data_kantin = {
'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Es Teh', None],
'harga': [12000, 4000, 10000, 4000, 8000],
'terjual': [23, 40, None, 35, 18]
 }
df = pd.DataFrame(data_kantin)
print(df)
#Analisis
#  Kolom yang memiliki data kosong adalah menu (indeks ke-4) dan terjual (indeks ke-2).
#  Risikonya jika langsung dianalisis tanpa dibersihkan adalah perhitungan matematika menjadi tidak akurat
#  (misalnya total pendapatan dari harga * terjual akan menghasilkan nilai kosong/ NaN), serta informasi menu
#  menjadi tidak jelas karena ada data transaksi yang tidak diketahui nama barangnya.


#Latihan 3: Data Loading & Inspection
df = pd.read_csv('data_kantin.csv')
print(df.head()) 
print(df.info())
print(df.describe()) 
print(df.shape) 
#Analisis
#  Kolom yang jumlah non-null-nya lebih sedikit adalah
#  kolom menu dan terjual (berdasarkan data kantin sebelumnya).
#  Artinya, kedua kolom tersebut memiliki nilai kosong (missing values / NaN),
#  sehingga ada beberapa baris data yang belum terisi secara lengkap dan perlu dibersihkan sebelum dianalisis lebih lanjut.

#Latihan 4: Menangani Missing Value
print(df.isnull().sum()) 
df['terjual'] = df['terjual'].fillna(0) 
df = df.dropna(subset=['menu']) 
# Analisis
# terjual diisi 0 (fillna): Karena data angka bernilai kosong logis diasumsikan belum ada penjualan (0 unit), sehingga datanya masih bisa dihitung secara matematis tanpa merusak analisis.
# menu dihapus (dropna): Karena menu adalah identitas utama item (kategori). Jika nama menunya tidak ada, data angka di baris tersebut menjadi tidak bermakna/tidak dapat diidentifikasi milik produk mana.
 
 #Latihan 5: Menangani Duplikat dan Tipe Data
print(df.duplicated().sum()) 
df = df.drop_duplicates()
df['harga'] = df['harga'].astype(int) 
print(df.dtypes)
#Analisi
# Jumlah baris: Berkurang dari 5 baris menjadi 3 baris (karena ada 1 data ganda 'Es Teh' yang dihapus dan 1 baris ber-menu kosong yang sudah dibuang di latihan sebelumnya).
# Pentingnya tipe data (dtypes): Memastikan tipe data benar sangat krusial agar fungsi analisis dan operasi matematika bekerja tepat.
#  Jika harga bertipe string (teks), operasi seperti penjumlahan atau perkalian akan gagal atau salah (misalnya teks "4000" + "4000" menjadi "40004000", bukan 8000).


# #Latihan 6: Data Manipulation (Filtering, Sorting, Groupby)
laris = df[df['terjual'] > 20] 
urut = df.sort_values(by='terjual', ascending=False) 
df['total_pendapatan'] = df['harga'] * df['terjual']
ringkasan = df.groupby('menu')['total_pendapatan'].sum()
# Menu pendapatan tertinggi: Nasi Goreng (dengan total pendapatan Rp276.000, hasil dari 12.000 × 23).
# Manfaat pengambilan keputusan: Informasi ini membantu pengelola kantin untuk memprioritaskan stok bahan baku menu paling menguntungkan agar tidak kehabisan,
#  serta menentukan strategi promosi atau evaluasi harga untuk menu-menu lain yang peminatnya masih rendah.