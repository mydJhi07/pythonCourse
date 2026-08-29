# Arithmetic & Math

# ==========================================
# MATERI LENGKAP: ARITHMETIC & MATH DI PYTHON
# (Diperkaya dari referensi Bro Code)
# ==========================================
import math # Selalu letakkan import ini di baris paling atas untuk fungsi matematika lanjutan

# ------------------------------------------
# 1. OPERATOR ARITMATIKA DASAR
# ------------------------------------------
print("--- 1. OPERATOR ARITMATIKA ---")
friends = 5

print(f"Penjumlahan (+)      : 5 + 1 = {friends + 1}")
print(f"Pengurangan (-)      : 5 - 2 = {friends - 2}")
print(f"Perkalian (*)        : 5 * 3 = {friends * 3}")
print(f"Pembagian (/)        : 5 / 2 = {friends / 2}")     # Hasilnya selalu Float (desimal)
print(f"Pangkat (**)         : 5 ** 2 = {friends ** 2}")   # 5 pangkat 2
print(f"Modulo (%)           : 5 % 2 = {friends % 2}")     # Sisa hasil bagi (Berguna untuk cek ganjil/genap)
print()


# ------------------------------------------
# 2. AUGMENTED ASSIGNMENT OPERATORS
# ------------------------------------------
# Ini adalah cara singkat (shortcut) untuk memperbarui nilai sebuah variabel.
print("--- 2. AUGMENTED ASSIGNMENT ---")
friends = 0
print(f"Jumlah teman awal: {friends}")

friends += 1  # Sama persis dengan: friends = friends + 1
print(f"Setelah += 1 : {friends}")

friends *= 3  # Sama persis dengan: friends = friends * 3
print(f"Setelah *= 3 : {friends}")
print()


# ------------------------------------------
# 3. FUNGSI MATEMATIKA BAWAAN (TANPA IMPORT)
# ------------------------------------------
# Fungsi ini sudah ada secara default di Python dan bisa langsung dipakai.
print("--- 3. FUNGSI MATEMATIKA BAWAAN ---")
x = 3.14
y = -4
z = 5

print(f"round(3.14) : {round(x)}")      # Output: 3 (Membulatkan ke bilangan bulat terdekat)
print(f"abs(-4)     : {abs(y)}")        # Output: 4 (Nilai mutlak / jarak dari nol)
print(f"pow(4, 3)   : {pow(4, 3)}")     # Output: 64 (4 pangkat 3, alternatif dari **)
print(f"max(x, y, z): {max(x, y, z)}")  # Output: 5 (Mencari nilai TERBESAR)
print(f"min(x, y, z): {min(x, y, z)}")  # Output: -4 (Mencari nilai TERKECIL)
print()


# ------------------------------------------
# 4. MODUL MATH (FUNGSI MATEMATIKA LANJUTAN)
# ------------------------------------------
# Memerlukan 'import math' di awal program.
print("--- 4. MODUL MATH ---")
angka = 9.9

print(f"math.pi     : {math.pi}")          # Output: 3.141592653589793 (Konstanta Pi)
print(f"math.e      : {math.e}")           # Output: 2.718281828459045 (Konstanta Eksponensial)
print(f"math.sqrt(9): {math.sqrt(9)}")     # Output: 3.0 (Akar kuadrat / Square root)
print(f"math.ceil(9.1): {math.ceil(9.1)}") # Output: 10 (Selalu dibulatkan ke ATAS / Ceiling)
print(f"math.floor(9.9): {math.floor(9.9)}")# Output: 9 (Selalu dibulatkan ke BAWAH / Floor)
print()


# ------------------------------------------
# 5. LATIHAN PRAKTIS (Diadaptasi dari Video)
# ------------------------------------------
print("--- 5. LATIHAN PRAKTIS ---")

# Latihan A: Menghitung Keliling Lingkaran (Circumference) -> Rumus: C = 2 * pi * r
radius = 5.0 # Misalnya kita pakai input statis 5.0 (Bisa diganti dengan input() dari user)
circumference = 2 * math.pi * radius
print(f"Keliling lingkaran (r={radius}): {round(circumference, 2)} cm")  # dibulatkan hingga 2 desimal

# Latihan B: Menghitung Luas Lingkaran (Area) -> Rumus: A = pi * r^2
area = math.pi * pow(radius, 2)
print(f"Luas lingkaran (r={radius})    : {round(area, 2)} cm^2")

# Latihan C: Menghitung Sisi Miring Segitiga Siku-siku (Hypotenuse) -> Rumus: c = √(a^2 + b^2)
a = 3.0
b = 4.0
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Sisi miring (a={a}, b={b})  : {c}")