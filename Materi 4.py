# ==========================================
# MATERI LENGKAP: USER INPUT DI PYTHON
# ==========================================
# Sebuah fungsi yang meminta pengguna untuk memasukkan data, lalu data akan dikembalikan dalam bentuk string
# Fungsi input() akan menghentikan sementara program Anda
# dan menunggu pengguna mengetikkan sesuatu di terminal,
# lalu menekan tombol ENTER.

# ------------------------------------------
# 1. PENGGUNAAN DASAR
# ------------------------------------------
print("--- 1. PENGGUNAAN DASAR ---")
# Di dalam kurung, kita bisa memasukkan teks (string) sebagai
# "prompt" atau pesan instruksi untuk pengguna.
nama_depan = input("Masukkan nama depan Anda: ")
nama_belakang = input("Masukkan nama belakang Anda: ")

print(f"Selamat datang, {nama_depan} {nama_belakang}!\n")


# ------------------------------------------
# 2. MEMBERSIHKAN INPUT PENGGUNA SECARA LANGSUNG
# ------------------------------------------
print("--- 2. MEMBERSIHKAN INPUT ---")
# Pengguna sering kali tidak sengaja mengetik spasi berlebih atau
# menggunakan huruf besar/kecil yang tidak beraturan.
# Kita bisa langsung menempelkan String Methods seperti .strip()
# dan .lower() tepat setelah fungsi input().

# Contoh: Kita ingin memastikan jawabannya huruf kecil semua dan tanpa spasi berlebih
konfirmasi = input(
    "Apakah Anda yakin ingin keluar? (ya/tidak): ").strip().lower()

# Jika pengguna mengetik: "   YA  ", "Ya", atau "ya ",
# kodenya akan otomatis membersihkannya menjadi "ya".
print(f"Sistem mencatat jawaban Anda: '{konfirmasi}'\n")


# ------------------------------------------
# 3. MENGGABUNGKAN INPUT DAN KONVERSI ANGKA
# ------------------------------------------
print("--- 3. INPUT ANGKA (RECAP) ---")
# Selalu ingat: input() MENGHASILKAN STRING.
# Jika butuh perhitungan, bungkus dengan int() atau float().

harga_barang = float(input("Masukkan harga barang: Rp "))
jumlah_beli = int(input("Beli berapa buah? "))

total_bayar = harga_barang * jumlah_beli
# Mencetak dengan format pemisah ribuan (, atau _)
print(f"Total yang harus dibayar: Rp {total_bayar:,.2f}\n")


# ------------------------------------------
# 4. MENGAMBIL BANYAK INPUT DALAM SATU BARIS (ADVANCED)
# ------------------------------------------
print("--- 4. MULTIPLE INPUT (SATU BARIS) ---")
# Menggunakan fungsi .split(), kita bisa meminta pengguna memasukkan
# beberapa data sekaligus yang dipisahkan oleh spasi.

data = input(
    "Masukkan Nama, Umur, dan Kota asal (pisahkan dengan spasi): ").split()

# Input pengguna akan dipecah menjadi List (Daftar)
# Misal pengguna mengetik: Budi 25 Jakarta
nama_user = data[0]
umur_user = int(data[1])  # Jangan lupa dikonversi jika mau dipakai menghitung
kota_user = data[2]

print("--- Hasil Ekstrak Data ---")
print(f"Nama : {nama_user}")
print(f"Umur : {umur_user} tahun")
print(f"Kota : {kota_user}")
