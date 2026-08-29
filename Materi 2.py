# Variable

#  Variabel = wadah untuk suatu nilai (string, bilangan bulat, bilangan desimal, boolean); sebuah variabel berperilaku seolah-olah
#  ia adalah nilai yang dikandungnya

# STRING
first_name = "Muhammad"
print(first_name)

# gunakan ini untuk menampilkan teks bersamaan dengan variabel
print(f"Hello {first_name}")

student_count = 1000
rating = 4.99
is_published = False
my_name = "Muhammad Yudha Damanhuri"
print(student_count)

# ==========================================
# PENJELASAN TIPE DATA PRIMITIF DI PYTHON
# ==========================================

# 1. INTEGER (int)
# Penjelasan: Tipe data untuk bilangan bulat, tanpa angka desimal.
# Bisa berupa bilangan positif, negatif, atau nol.
jumlah_kucing = 3
suhu_kutub = -15
# Komen: Variabel 'jumlah_kucing' dan 'suhu_kutub' adalah integer karena tidak memiliki koma/titik desimal.
print(
    f"Saya punya {jumlah_kucing} kucing dan suhu di kutub adalah {suhu_kutub} derajat.")


# 2. FLOAT (float)
# Penjelasan: Tipe data untuk bilangan desimal atau pecahan.
# Di Python, penulisan desimal menggunakan titik (.), BUKAN koma (,).
berat_badan = 65.5
harga_diskon = 10.99
# Komen: Variabel di atas adalah float. Jika Anda menulis 65,5 (pakai koma), Python akan menganggapnya sebagai tuple, bukan float.
print(
    f"Berat badan ideal adalah {berat_badan} kg dengan harga diskon {harga_diskon} dollar.")


# 3. STRING (str)
# Penjelasan: Tipe data untuk teks, kata, atau kalimat.
# Nilainya WAJIB diapit oleh tanda kutip tunggal ('...') atau kutip ganda ("...").
nama_pengguna = "Budi Santoso"
status_hari_ini = 'Semangat belajar Python!'
# Komen: Apapun yang berada di dalam tanda kutip akan dianggap string, meskipun itu angka (contoh: "123" adalah string, bukan integer).
print(f"Halo {nama_pengguna}, {status_hari_ini}")


# 4. BOOLEAN (bool)
# Penjelasan: Tipe data logika yang HANYA memiliki dua nilai: True (Benar) atau False (Salah).
# Ingat: Huruf pertama wajib kapital (T atau F).
sedang_login = True
punya_hutang = False
# Komen: Boolean sangat sering digunakan untuk percabangan/logika (if-else).
print(f"Status login: {sedang_login} | Apakah punya hutang? {punya_hutang}")


# 5. NONETYPE (None)
# Penjelasan: Tipe data khusus untuk merepresentasikan ketiadaan nilai (null/kosong).
# Sama seperti Boolean, huruf pertamanya wajib kapital (N).
data_sementara = None
# Komen: Biasanya digunakan jika kita ingin membuat variabel tapi belum tahu mau diisi apa.
print(f"Isi data sementara saat ini adalah: {data_sementara}")


# ==========================================
# BONUS: CARA MENGECEK TIPE DATA
# ==========================================
# Jika Anda ragu suatu variabel itu tipe datanya apa, Anda bisa menggunakan fungsi type()

print("\n--- Hasil Pengecekan Tipe Data ---")
print(type(jumlah_kucing))    # Output: <class 'int'>
print(type(berat_badan))      # Output: <class 'float'>
print(type(nama_pengguna))    # Output: <class 'str'>
print(type(sedang_login))     # Output: <class 'bool'>
print(type(data_sementara))   # Output: <class 'NoneType'>
