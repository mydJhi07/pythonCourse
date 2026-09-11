# 1. Konsep Dasar 2D List (List di dalam List)
# Mirip dengan tabel atau grid Excel yang memiliki baris (rows) dan kolom (columns).
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Menggabungkan ketiga list 1D di atas menjadi sebuah 2D List
groceries = [fruits, vegetables, meats]

# 2. Mengakses Elemen dengan Indeks Ganda: [row][column]
# Jika hanya memanggil 1 indeks, Python akan mencetak seluruh isi baris tersebut.
print(f"Isi Baris 0 (Fruits): {groceries[0]}") 

# Untuk mengakses item spesifik, gunakan [baris][kolom]. Ingat, indeks dimulai dari 0.
print(f"Baris 0, Kolom 0: {groceries[0][0]}") # Output: apple
print(f"Baris 1, Kolom 2: {groceries[1][2]}") # Output: potatoes
print(f"Baris 2, Kolom 1: {groceries[2][1]}") # Output: fish

# 3. Menampilkan 2D List dengan Nested Loop
print("\n--- Tabel Groceries ---")
# Outer loop menelusuri setiap baris (list individu) di dalam groceries
for collection in groceries:
    # Inner loop menelusuri setiap makanan (item) di dalam baris tersebut
    for food in collection:
        print(food, end=" ") # Cetak menyamping
    print() # Pindah ke baris baru setelah satu kategori (baris) selesai


# 4. 2D Tuples: Contoh Kasus Numpad Telepon
# Tuple (menggunakan kurung biasa) digunakan karena struktur tombol telepon tidak akan pernah berubah (immutable).
numpad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

print("\n--- Layout Numpad ---")
# Menelusuri 2D Tuple dengan teknik yang persis sama
for row in numpad:
    for num in row:
        print(num, end=" ")
    print()

"""
    Arsitektur Matriks / Grid (2D Collections): Sederhananya, 2D collection adalah kumpulan (collection) yang menampung kumpulan
    lainnya di dalamnya. Konsep ini adalah solusi paling esensial jika Anda perlu membuat data terstruktur berbentuk grid, 
    matriks, atau tabel, di mana struktur dasarnya terdiri atas baris (rows) horizontal dan kolom (columns) vertikal.

    Akses Koordinat Ganda ([row][column]): Pada list 1D biasa, Anda cukup menggunakan satu indeks. Namun pada 2D list, 
    pemanggilan satu indeks (misal: groceries[0]) hanya akan mengeluarkan data mentah berupa baris utuh secara keseluruhan. 
    Untuk mengekstrak elemen spesifik yang tertanam di dalamnya, Anda wajib menggunakan sintaks indeks ganda bagaikan menentukan
    titik koordinat: kurung siku pertama mencari letak barisnya, kurung siku kedua menunjuk kolomnya.

    Kewajiban Nested Loop untuk Ekstraksi Total: Mencetak isi matriks tidak bisa dilakukan hanya dengan satu for loop. Sebuah 
    loop tunggal hanya akan melempar keluar baris-baris kasar. Oleh karena itu, kita harus memasang nested loop 
    (loop di dalam loop). Outer loop bertugas memegang baris saat itu, kemudian menyerahkannya pada inner loop untuk dibedah
    dan dicetak isi karakternya satu demi satu secara mendetail.

    Fleksibilitas Koleksi Lintas Tipe: Python tidak membatasi 2D collections hanya pada List. Anda bebas memformulasikan 2D 
    Tuples, 2D Sets, atau List yang berisi sekumpulan Tuples. Dalam contoh pembuatan numpad (papan angka telepon), menggunakan
    2D Tuple jauh lebih logis karena susunan tombol tersebut tidak boleh bisa diubah, serta Tuples memberikan kecepatan 
    pemrosesan yang lebih baik dibanding List.
"""