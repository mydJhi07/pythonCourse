# ==========================================
# MATERI LENGKAP: STRING INDEXING DI PYTHON
# (Diadaptasi dari referensi Bro Code)
# ==========================================

credit_number = "1234-5678-9012-3456"
print(f"Nomor Kartu Asli: {credit_number}\n")

# ------------------------------------------
# 1. INDEXING DASAR (MENGAMBIL 1 KARAKTER)
# ------------------------------------------
# Komputer selalu mulai menghitung dari angka 0.
print("--- 1. INDEXING DASAR ---")
print(f"Karakter pertama [0] : {credit_number[0]}") # Output: 1
print(f"Karakter kedua [1]   : {credit_number[1]}") # Output: 2

# Indeks Negatif: Sangat berguna untuk mengambil dari belakang 
# tanpa perlu tahu panjang total stringnya. (-1 adalah karakter paling akhir)
print(f"Karakter terakhir [-1]       : {credit_number[-1]}") # Output: 6
print(f"Karakter kedua dari akhir [-2] : {credit_number[-2]}") # Output: 5
print()


# ------------------------------------------
# 2. SLICING (MENGAMBIL RENTANG KARAKTER)
# ------------------------------------------
# Menggunakan format [start:stop]. Ingat, batas 'stop' TIDAK diikutkan.
print("--- 2. SLICING ---")
print(f"Ambil indeks 0 sampai 3 [0:4] : {credit_number[0:4]}") # Output: 1234
print(f"Ambil indeks 5 sampai 8 [5:9] : {credit_number[5:9]}") # Output: 5678

# Shorthand (Cara Singkat)
print(f"Dari awal sampai indeks 3 [:4] : {credit_number[:4]}") # Sama dengan [0:4]
print(f"Dari indeks 5 sampai ujung [5:] : {credit_number[5:]}") # Output: 5678-9012-3456
print()


# ------------------------------------------
# 3. STEP (LOMPATAN)
# ------------------------------------------
# Menggunakan format [start:stop:step].
print("--- 3. STEP (LOMPATAN) ---")

# Jika start dan stop dikosongkan (::), Python mengambil dari ujung ke ujung.
print(f"Ambil setiap 2 karakter [::2] : {credit_number[::2]}")  # Output: 13-6891-46
print(f"Ambil setiap 3 karakter [::3] : {credit_number[::3]}")  # Output: 14580246

# Trik Sakti Python: Membalikkan string menggunakan step -1
print(f"Balikkan string [::-1]        : {credit_number[::-1]}") # Output: 6543-2109-8765-4321
print()

# ==========================================
# LATIHAN PRAKTIS: MENSOR NOMOR KARTU KREDIT
# ==========================================
# Di dunia nyata, kita sering harus menyembunyikan nomor kartu kredit 
# dan hanya menampilkan 4 digit terakhirnya saja.

print("--- LATIHAN: SENSOR KARTU KREDIT ---")
# Kita ambil 4 digit terakhir menggunakan indeks negatif
last_digits = credit_number[-4:] 

# Kita gabungkan dengan teks sensor (karakter 'X')
sensor_kredit = f"XXXX-XXXX-XXXX-{last_digits}"
print(f"Nomor Kartu Disensor: {sensor_kredit}")