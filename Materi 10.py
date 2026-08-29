# ==========================================
# MATERI LENGKAP: CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# (Diadaptasi dari Bro Code & Materi Pelengkap)
# ==========================================

# Ingat Rumusnya:
# X if (Kondisi True) else Y

# ------------------------------------------
# 1. CEK ANGKA POSITIF / NEGATIF
# ------------------------------------------
print("--- 1. POSITIF / NEGATIF ---")
num = 5

# Cara tradisional (4 baris):
# if num > 0:
#     print("Positif")
# else:
#     print("Negatif")

# Cara Conditional Expression (1 baris):
print("Positif" if num > 0 else "Negatif")  # Output: Positif
print()


# ------------------------------------------
# 2. CEK GANJIL / GENAP (EVEN OR ODD)
# ------------------------------------------
print("--- 2. GANJIL / GENAP ---")
angka = 6
# Memasukkan hasil evaluasi langsung ke dalam variabel 'result'
result = "Genap (Even)" if angka % 2 == 0 else "Ganjil (Odd)"

print(f"Angka {angka} adalah angka {result}.") 
# Output: Angka 6 adalah angka Genap (Even).
print()


# ------------------------------------------
# 3. MENCARI NILAI MAX DAN MIN
# ------------------------------------------
print("--- 3. NILAI MAX DAN MIN ---")
a = 6
b = 7

# Jika a lebih besar dari b, kembalikan a. Jika tidak, kembalikan b.
max_num = a if a > b else b
min_num = a if a < b else b

print(f"Nilai Maksimal antara {a} dan {b} adalah {max_num}") # Output: 7
print(f"Nilai Minimal antara {a} dan {b} adalah {min_num}")  # Output: 6
print()


# ------------------------------------------
# 4. STATUS BERDASARKAN UMUR & HAK AKSES
# ------------------------------------------
print("--- 4. STATUS & HAK AKSES ---")
age = 25
user_role = "admin"

status = "Dewasa (Adult)" if age >= 18 else "Anak-anak (Child)"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(f"Status umur Anda : {status}")
print(f"Hak akses sistem : {access_level}")
print()


# ==========================================
# MATERI PELENGKAP (ADVANCED)
# ==========================================

# ------------------------------------------
# 5. MENGGUNAKANNYA LANGSUNG DI DALAM F-STRING
# ------------------------------------------
# Trik yang sangat sering dipakai oleh programmer profesional untuk menghemat baris.
print("--- 5. CONDITIONAL EXPRESSION DALAM F-STRING ---")

is_vip = True
# Anda bisa menyematkan logikanya langsung di dalam kurung kurawal {} f-string!
print(f"Harga tiket Anda: Rp {'100.000' if is_vip else '250.000'}")
# Output: Harga tiket Anda: Rp 100.000