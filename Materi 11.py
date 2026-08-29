# ==========================================
# MATERI LENGKAP: STRING METHODS DI PYTHON
# (Diadaptasi dari referensi Bro Code)
# ==========================================

nama = "Bro Code"

print("--- 1. MENCARI PANJANG STRING ---")
# len() adalah fungsi bawaan untuk menghitung jumlah karakter (termasuk spasi).
panjang_nama = len(nama)
print(f"Panjang dari '{nama}' adalah {panjang_nama} karakter.")
print()

print("--- 2. MENCARI POSISI KARAKTER (.find & .rfind) ---")
# .find() mencari kemunculan PERTAMA dari sebuah karakter/kata.
# Jika tidak ditemukan, hasilnya adalah -1. Ingat: Indeks dimulai dari 0.
print(f"Posisi huruf 'o' pertama (.find)  : {nama.find('o')}")

# .rfind() mencari kemunculan TERAKHIR (dari belakang / reverse).
print(f"Posisi huruf 'o' terakhir (.rfind): {nama.rfind('o')}")

# Jika karakter tidak ada:
print(f"Mencari huruf 'z'                 : {nama.find('z')}") # Output: -1
print()

print("--- 3. MANIPULASI HURUF BESAR/KECIL ---")
teks = "belajar PYTHON"
print(f"Asli          : {teks}")
print(f".capitalize() : {teks.capitalize()}") # Hanya huruf PALING AWAL yang jadi besar
print(f".upper()      : {teks.upper()}")      # Semua huruf jadi BESAR
print(f".lower()      : {teks.lower()}")      # Semua huruf jadi kecil
print()

print("--- 4. MENGHITUNG DAN MENGGANTI KARAKTER ---")
# .count() menghitung berapa kali suatu karakter muncul.
# .replace() mengganti suatu karakter dengan karakter lain.
no_hp = "123-456-7890"

print(f"Nomor HP asli              : {no_hp}")
print(f"Jumlah tanda strip (.count): {no_hp.count('-')}")

# Kita bisa menggunakan .replace() untuk menghapus strip dengan menggantinya menjadi spasi (" ")
# atau menghapusnya sama sekali dengan string kosong ("").
no_hp_spasi = no_hp.replace("-", " ")
no_hp_bersih = no_hp.replace("-", "")

print(f"Ganti strip dengan spasi   : {no_hp_spasi}")
print(f"Hapus strip sepenuhnya     : {no_hp_bersih}")
print()

print("--- 5. PENGECEKAN KONTEN STRING (BOOLEAN) ---")
# Menghasilkan True atau False.
angka = "12345"
huruf = "Spongebob"
campuran = "Bro Code" # Mengandung spasi

# .isdigit() mengecek apakah string HANYA berisi angka
print(f"Apakah '{angka}' hanya angka? (.isdigit) : {angka.isdigit()}")

# .isalpha() mengecek apakah string HANYA berisi huruf alfabet
# SPASI tidak dihitung sebagai alfabet, jadi "Bro Code" akan False.
print(f"Apakah '{huruf}' hanya huruf? (.isalpha)  : {huruf.isalpha()}")
print(f"Apakah '{campuran}' hanya huruf? (.isalpha) : {campuran.isalpha()}")
print()


# ==========================================
# LATIHAN PRAKTIS: VALIDASI USERNAME
# ==========================================
# Aturan Username:
# 1. Tidak boleh lebih dari 12 karakter
# 2. Tidak boleh mengandung spasi
# 3. Tidak boleh mengandung angka

print("--- LATIHAN: VALIDASI USERNAME ---")
# Coba ubah nilai ini untuk mengetes validasi:
username = "Bro Code 123" 

# Jika Anda ingin mencoba input interaktif, hapus tanda '#' di bawah ini:
# username = input("Masukkan username Anda: ")

if len(username) > 12:
    print(f"❌ Username '{username}' gagal: Tidak boleh lebih dari 12 karakter.")
elif username.find(" ") != -1:
    # Jika .find(" ") tidak sama dengan -1, berarti ADA spasi di dalamnya
    print(f"❌ Username '{username}' gagal: Tidak boleh mengandung spasi.")
elif not username.isalpha():
    # Jika tidak full alfabet (berarti ada angka/simbol lain)
    print(f"❌ Username '{username}' gagal: Tidak boleh mengandung angka/simbol.")
else:
    print(f"✅ Selamat datang, {username}!")

# ==========================================
# BONUS (DARI REFERENSI BRO CODE)
# ==========================================
# Jika Anda ingin melihat DAFTAR LENGKAP semua string method yang ada di Python,
# Anda bisa menggunakan fungsi help(). 
# Hapus tanda '#' pada baris di bawah untuk melihat dokumentasinya:

# print(help(str))