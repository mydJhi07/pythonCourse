# ==========================================
# MATERI LENGKAP: TYPE CONVERSION (KONVERSI TIPE DATA) & INPUT
# ==========================================

# ------------------------------------------
# 1. KONVERSI DASAR (int, float, str)
# ------------------------------------------
print("--- 1. KONVERSI DASAR PADA VARIABEL ---")
tahun_str = "2001"
desimal = 9.99
angka_bulat = 5

# String ke Integer & Float
print(f"String '2001' ke Integer   : {int(tahun_str)}")     # Output: 2001
print(f"String '2001' ke Float     : {float(tahun_str)}")   # Output: 2001.0

# Float ke Integer (Membuang angka di belakang koma)
print(f"Float 9.99 ke Integer      : {int(desimal)}")       # Output: 9

# Integer ke Float & String
print(f"Integer 5 ke Float         : {float(angka_bulat)}")  # Output: 5.0
# Output: 5 (bisa digabung dengan teks lain pakai +)
print("Angka ke String            : " + str(angka_bulat))
print()


# ------------------------------------------
# 2. KONVERSI KE BOOLEAN (TRUTHY & FALSY)
# ------------------------------------------
print("--- 2. KONVERSI BOOLEAN (TRUTHY & FALSY) ---")
# Falsy: Nilai yang dianggap False (kosong/nol)
print(f"bool(0)    : {bool(0)}")       # Output: False
print(f"bool('')   : {bool('')}")      # Output: False (String kosong)

# Truthy: Nilai yang dianggap True (berisi/selain nol)
print(f"bool(1)    : {bool(1)}")       # Output: True
print(f"bool(-5)   : {bool(-5)}")      # Output: True
print(f"bool('Hai'): {bool('Hai')}")   # Output: True
print("\n" + "="*40 + "\n")


# ==========================================
# BAGIAN INTERAKTIF: TYPE CONVERSION DENGAN INPUT()
# ==========================================
# CATATAN: Program akan berhenti sejenak di sini.
# Silakan klik terminal Anda dan ketikkan jawaban untuk melanjutkan program!

print("--- 3. INPUT STRING (TANPA KONVERSI) ---")
# input() selalu menghasilkan tipe data String secara bawaan.
nama = input("Masukkan nama Anda: ")
print(f"Halo {nama}, selamat belajar Python!\n")


# ------------------------------------------
# 4. INPUT INTEGER & FLOAT (CARA SINGKAT)
# ------------------------------------------
print("--- 4. INPUT ANGKA MATEMATIKA ---")
# Konversi langsung digabung dengan input()
# Format: tipe_data(input("Pesan: "))

# Mengambil input integer
tahun_lahir = int(input("Masukkan tahun lahir Anda (contoh: 2001): "))
umur = 2026 - tahun_lahir  # Menggunakan tahun 2026 sebagai patokan
print(f"Umur Anda saat ini adalah {umur} tahun.\n")

# Mengambil input float
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter, misal 1.75): "))
bmi = berat / (tinggi ** 2)
print(f"Nilai BMI Anda adalah: {bmi:.2f}\n")


# ------------------------------------------
# 5. MENGATASI ERROR INPUT (TRY - EXCEPT)
# ------------------------------------------
print("--- 5. MENGATASI ERROR INPUT ---")
# Jika program meminta angka tapi user mengetik huruf, program akan ERROR (ValueError).
# Gunakan try-except untuk mencegah program crash (berhenti paksa).

try:
    # Program mencoba menjalankan blok ini dulu
    jumlah_kucing = int(input("Berapa jumlah kucing Anda? (Harus angka): "))
    total_kaki = jumlah_kucing * 4
    print(f"Total kaki kucing Anda ada {total_kaki} kaki.")

except ValueError:
    # Jika terjadi error (karena user mengetik huruf), blok ini yang dijalankan
    print("Oops! Terjadi kesalahan. Anda harus memasukkan angka (contoh: 3), bukan teks.")
