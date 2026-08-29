# ==========================================
# MATERI LENGKAP: LOGICAL OPERATORS DI PYTHON
# (Diadaptasi dari Bro Code & Materi Pelengkap)
# ==========================================

print("--- 1. OPERATOR 'or' ---")
# 'or' akan menghasilkan True jika MINIMAL SALAH SATU kondisi bernilai True.
# Kasus: Mengecek apakah acara outdoor harus dibatalkan.
temp = 25           # Suhu dalam Celcius
is_raining = False  # Apakah sedang hujan?

# Jika suhu di atas 35 (terlalu panas) ATAU di bawah 0 (terlalu dingin) ATAU sedang hujan
if temp > 35 or temp < 0 or is_raining:
    print("Acara outdoor dibatalkan. ❌")
else:
    print("Acara outdoor tetap berjalan sesuai jadwal. ✅")
print()


print("--- 2. OPERATOR 'and' ---")
# 'and' akan menghasilkan True HANYA JIKA SEMUA kondisi bernilai True.
# Kasus: Menentukan pakaian berdasarkan cuaca.
temp = 30
is_sunny = True

# Keduanya (suhu >= 28 DAN cerah) harus True agar blok kode ini dijalankan
if temp >= 28 and is_sunny:
    print("Di luar sangat panas dan cerah. 🥵☀️")
elif temp <= 0 and is_sunny:
    print("Di luar dingin tapi cerah. 🥶☀️")
print()


print("--- 3. OPERATOR 'not' ---")
# 'not' akan membalikkan nilai boolean. True menjadi False, dan False menjadi True.
# Kasus: Jika tidak cerah, berarti berawan.
is_sunny = False

# Daripada menulis "if is_sunny == False:", programmer Python lebih suka menulis "if not is_sunny:"
if not is_sunny:
    print("Di luar sedang berawan. ☁️")
else:
    print("Di luar sedang cerah. ☀️")
print()


# ==========================================
# MATERI PELENGKAP (ADVANCED)
# ==========================================

print("--- 4. CHAINING COMPARISONS (CARA SINGKAT PYTHON) ---")
# Di video, Bro Code menunjukkan cara mengecek rentang angka.
# Secara logika biasa, kita menulis: (temp > 0 and temp < 28)
# Namun Python punya fitur khusus untuk menyingkatnya seperti bahasa matematika!

temp = 20
is_sunny = True

# Cara biasa:
# if temp > 0 and temp < 28 and is_sunny:

# Cara Singkat Python (Chaining):
if 0 < temp < 28 and is_sunny:
    print("Cuaca di luar hangat dan cerah. Sangat pas! 😎☀️")
print()


print("--- 5. SHORT-CIRCUIT EVALUATION (LOGIKA CEPAT PYTHON) ---")
# Python itu pintar. Ia menggunakan evaluasi "Short-Circuit" (Jalan Pintas).
# - Pada 'and': Jika kondisi pertama sudah False, Python TIDAK AKAN mengecek kondisi kedua (karena pasti hasil akhirnya False).
# - Pada 'or' : Jika kondisi pertama sudah True, Python TIDAK AKAN mengecek kondisi kedua (karena pasti hasil akhirnya True).

angka = 10
pembagi = 0

# Contoh pada 'and':
# Python mengecek (pembagi != 0) dulu. Karena hasilnya False, pengecekan (angka / pembagi > 1) 
# langsung DIBATALKAN. Program Anda selamat dari error 'ZeroDivisionError' (dibagi nol)!
if pembagi != 0 and (angka / pembagi > 1):
    print("Pembagian berhasil.")
else:
    print("Evaluasi short-circuit menyelamatkan program dari error dibagi nol!")