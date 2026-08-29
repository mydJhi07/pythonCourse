# ==========================================
# MATERI LENGKAP: PENGAMBILAN KEPUTUSAN (IF STATEMENTS)
# ==========================================

# ------------------------------------------
# 1. PENGGUNAAN DASAR (IF, ELIF, DAN ELSE)
# ------------------------------------------
# PENTING: Python membaca dari atas ke bawah. Kondisi yang paling 
# spesifik harus diletakkan paling atas. Perhatikan juga indentasi (Tab).
print("--- 1. PENGGUNAAN DASAR ---")

age = 25 # Coba ganti angka ini untuk melihat hasil yang berbeda

if age >= 100:
    print("Anda terlalu tua untuk mendaftar.")
elif age >= 18:
    print("Pendaftaran berhasil. Anda sudah cukup umur!")
elif age < 0:
    print("Anda bahkan belum lahir!")
else:
    # else adalah pilihan terakhir jika semua kondisi di atas salah (False)
    print("Maaf, Anda harus berusia 18 tahun ke atas.")
print()


# ------------------------------------------
# 2. PERBANDINGAN TEKS & PENGECEKAN KOSONG
# ------------------------------------------
# Gunakan == (Sama dengan GANDA) untuk membandingkan kesamaan nilai.
print("--- 2. PERBANDINGAN TEKS ---")

response = "Y"
name = ""

# Mengecek teks
if response == "Y":
    print("Pesanan Anda segera diproses.")
elif response == "N":
    print("Pesanan dibatalkan.")

# Mengecek string kosong
if name == "":
    print("Peringatan: Nama tidak boleh kosong!")
else:
    print(f"Halo, {name}!")
print()


# ------------------------------------------
# 3. OPERATOR LOGIKA (AND, OR, NOT)
# ------------------------------------------
# Digunakan untuk mengecek lebih dari satu kondisi sekaligus.
print("--- 3. OPERATOR LOGIKA ---")

nilai = 85
kehadiran = 90
punya_kupon = False
hari_diskon = True
sedang_hujan = False

# AND: KEDUA kondisi wajib True
if nilai >= 80 and kehadiran >= 80:
    print("Selamat, Anda Lulus Cumlaude!")

# OR: SALAH SATU kondisi True saja sudah cukup
if punya_kupon or hari_diskon:
    print("Anda mendapatkan potongan harga!")

# NOT: Membalikkan kondisi (True jadi False, sebaliknya)
if not sedang_hujan:
    print("Cuaca cerah, mari pergi keluar!")
print()


# ------------------------------------------
# 4. NESTED IF (IF BERSARANG)
# ------------------------------------------
# Menaruh blok 'if' di dalam 'if'. Sangat berguna jika pengecekan 
# kedua hanya boleh dilakukan jika pengecekan pertama berhasil.
print("--- 4. NESTED IF ---")

umur_pengemudi = 20
punya_sim = True

# Pengecekan Level 1
if umur_pengemudi >= 18:
    print("Umur mencukupi untuk mengemudi.")
    
    # Pengecekan Level 2
    if punya_sim:
        print("Anda diizinkan mengemudi di jalan raya.")
    else:
        print("Namun, Anda belum memiliki SIM. Dilarang mengemudi!")
else:
    print("Anda belum cukup umur untuk mengemudi.")
print()


# ------------------------------------------
# 5. PENGGUNAAN BOOLEAN SECARA LANGSUNG
# ------------------------------------------
# Anda tidak perlu menulis "if is_online == True:".
print("--- 5. BOOLEAN LANGSUNG ---")

is_online = True

if is_online:
    print("Status: User sedang Online.")
else:
    print("Status: User sedang Offline.")
print()


# ------------------------------------------
# 6. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ------------------------------------------
# Cara elegan menulis if-else ke dalam SATU BARIS saja.
# Format: hasil_benar if kondisi else hasil_salah
print("--- 6. TERNARY OPERATOR ---")

suhu = 35
cuaca = "Panas" if suhu > 30 else "Dingin"

print(f"Suhu saat ini {suhu}°C, cuaca {cuaca}.")
print()


# ------------------------------------------
# 7. KATA KUNCI 'PASS'
# ------------------------------------------
# Jika Anda membuat blok 'if' tapi belum tahu mau mengisinya dengan apa,
# gunakan 'pass' agar program tidak error.
print("--- 7. PENGGUNAAN 'PASS' ---")

fitur_aktif = True

if fitur_aktif:
    pass # Menginstruksikan Python untuk melewati baris ini tanpa melakukan apa-apa
else:
    print("Fitur tidak aktif.")
    
print("Selesai (tidak ada error meskipun ada if yang isinya kosong).")