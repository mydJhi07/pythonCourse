import random;

# ==========================================
#   STUDI KASUS: GAME TEBAK ANGKA
# ==========================================
print("\n--- Python Number Guessing Game ---")

# Konfigurasi Awal
batas_bawah = 1
batas_atas = 100
# Mengunci satu angka sebagai kunci jawaban secara acak
jawaban = random.randint(batas_bawah, batas_atas) 

tebakan_ke = 0
sedang_bermain = True

# Inti Logika Permainan
while sedang_bermain:
    # Meminta input dan langsung memastikan apakah itu berupa angka
    tebakan = input(f"Tebak angka antara {batas_bawah} - {batas_atas}: ")
    
    # Validasi Input: Mencegah error jika pengguna mengetik huruf (misal: "pizza")
    if not tebakan.isdigit():
        print("Input tidak valid! Harap masukkan HANYA ANGKA.")
        continue # Lewati eksekusi di bawahnya, ulangi loop dari awal
    
    # Jika input aman, ubah tipe datanya menjadi Integer
    tebakan = int(tebakan)
    tebakan_ke += 1
    
    # Logika Pencocokan
    if tebakan < batas_bawah or tebakan > batas_atas:
        print(f"Tebakan Anda di luar jangkauan ({batas_bawah}-{batas_atas}).")
    elif tebakan < jawaban:
        print("Terlalu Rendah! Coba lagi.")
    elif tebakan > jawaban:
        print("Terlalu Tinggi! Coba lagi.")
    else:
        # Kondisi Menang
        print(f"BENAR! Jawabannya adalah {jawaban}.")
        print(f"Anda berhasil menebak dalam {tebakan_ke} percobaan.")
        sedang_bermain = False # Matikan loop