# ==========================================
# 1. LISTS (Daftar)
# Terurut, Bisa Diubah (Mutable), Mengizinkan Duplikat
# ==========================================
fruits_list = ["apple", "orange", "banana", "coconut"]

# A. Akses dan Slicing (Pemotongan)
# Indeks selalu dimulai dari 0.
print(fruits_list[0])       # Mengambil elemen pertama: apple
# Slicing: mengambil elemen dari indeks 0 hingga sebelum 3 (0, 1, 2)
print(fruits_list[0:3])     
# Step: melompat 2 langkah
print(fruits_list[::2])     
# Membalikkan urutan list sementara (Reverse Slicing)
print(fruits_list[::-1])    

# B. Modifikasi Elemen (Reassign)
fruits_list[0] = "pineapple" 

# C. Metode Manipulasi List
fruits_list.append("grape")      # Menambah 'grape' ke posisi paling akhir
fruits_list.insert(0, "mango")   # Menyisipkan 'mango' ke indeks 0, elemen lain bergeser
fruits_list.remove("orange")     # Mencari dan menghapus 'orange' pertama yang ditemukan
fruits_list.sort()               # Mengurutkan elemen secara alfabetis (A-Z)
fruits_list.reverse()            # Membalikkan posisi array saat ini secara fisik
# fruits_list.clear()            # Mengosongkan list menjadi []

# D. Utilitas Pencarian
print(fruits_list.index("banana")) # Mencari di indeks ke berapa "banana" berada
print(fruits_list.count("banana")) # Menghitung ada berapa banyak "banana" di dalam list


# ==========================================
# 2. SETS (Himpunan)
# Tidak Terurut, Sulit Diubah (Immutable elements), TANPA Duplikat
# ==========================================
fruits_set = {"apple", "orange", "banana", "coconut"}

# A. Modifikasi Set
fruits_set.add("pineapple")      # Ditambahkan ke posisi acak karena Set tidak memiliki indeks
fruits_set.remove("apple")       # Menghapus elemen spesifik
# pop() pada Set akan menghapus dan mengambil elemen yang posisinya paling depan. 
# Karena Set tidak terurut, elemen yang terhapus bersifat ACAK.
popped_item = fruits_set.pop()   

# B. Sifat Anti-Duplikat
# Jika kita memasukkan nilai yang sudah ada, Python akan mengabaikannya
fruits_set.add("banana")
fruits_set.add("banana")
print(fruits_set)                # Hanya akan tercetak satu "banana"


# ==========================================
# 3. TUPLES
# Terurut, TIDAK BISA Diubah (Immutable), Mengizinkan Duplikat
# ==========================================
fruits_tuple = ("apple", "orange", "banana", "coconut", "coconut")

# Karena Tuple dikunci mati (statis), metodenya sangat terbatas:
print(fruits_tuple.index("orange"))  # Mengembalikan posisi indeks dari "orange"
print(fruits_tuple.count("coconut")) # Menghitung kemunculan "coconut" (Output: 2)


# ==========================================
# FUNGSI UNIVERSAL UNTUK SEMUA COLLECTIONS
# ==========================================
# 1. Menghitung total elemen
total_items = len(fruits_list)

# 2. Membership Operator ('in') -> Mengembalikan True / False
is_available = "apple" in fruits_tuple

# 3. Iterasi (Perulangan)
for fruit in fruits_tuple:
    print(fruit)

# 4. Introspeksi Objek
# Melihat semua metode/fungsi yang tersedia untuk tipe data tertentu
print(dir(fruits_list))
# Melihat dokumentasi penjelasan dari fungsi-fungsi tersebut
# help(fruits_list)

"""
    Collection Data Types: List, Set, dan Tuple adalah variasi dari Collection—yakni sebuah struktur data yang dirancang untuk 
    menyimpan kumpulan nilai (elemen) di dalam satu wadah variabel. Perbedaan ketiganya terletak pada sintaks pembuatan, sifat 
    kekakuan data (apakah bisa diubah atau dikunci), dan cara Python mengelola memori/urutannya.

    List (Fleksibilitas Tertinggi): Diapit oleh []. List sangat lentur. Anda dapat menyisipkan (append/insert), menghapus 
    (remove/pop), menukar posisi indeks, hingga mengurutkan ulang (sort) isi di dalamnya secara dinamis kapan saja setelah list
    tersebut diciptakan. Karena sifatnya yang terurut (ordered), elemen selalu menempati alamat indeks yang pasti.

    Set (Koleksi Konstan Tanpa Indeks): Diapit oleh {}. Set membuang sistem indeks sepenuhnya. Konsekuensinya, data di dalamnya
    menjadi unordered (posisinya mengambang secara acak setiap kali dieksekusi). Aturan mutlak dari Set adalah tidak boleh ada 
    duplikasi. Jika Anda mencoba memasukkan data ganda, Python akan melebur duplikat tersebut. Anda tidak bisa mengedit nilai 
    yang sudah ada di dalamnya, tetapi Anda masih diperbolehkan untuk menambah atau menghapus elemen keseluruhan.

    Tuple (Koleksi yang Terkunci/Statis): Diapit oleh (). Tuple sangat mirip dengan List (terurut dan menerima duplikat), 
    tetapi dengan satu perbedaan radikal: ia bersifat immutable (terkunci secara permanen). Begitu sebuah Tuple lahir, isi
    elemennya tidak bisa ditambah, dihapus, atau dimodifikasi. Sebagai kompensasinya, karena ukurannya sudah dikunci
    mati oleh sistem, Python dapat memproses Tuple secara jauh lebih ringan dan cepat dibandingkan List.

"""