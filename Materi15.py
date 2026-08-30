# Program Kalkulator Bunga Majemuk (Compound Interest)

# 1. Deklarasi Variabel Dasar
# Menyediakan wadah kosong untuk menyimpan input pengguna.
principal = 0  # Modal awal
rate = 0      # Suku bunga (dalam persentase)
time = 0      # Jangka waktu (dalam tahun)

# 2. Input dan Validasi: Principal (Modal Awal)
# Menggunakan 'while loop' untuk memastikan bahwa modal awal yang dimasukkan harus lebih besar dari 0.
# Selama modal awal kurang dari atau sama dengan 0, program akan terus meminta input yang valid.
while principal <= 0:
    # Meminta input pengguna dan mengonversinya menjadi tipe float (bilangan desimal).
    principal = float(input("Enter the principal amount: "))

    # Jika input tidak valid (misal: negatif atau 0), tampilkan pesan kesalahan.
    if principal <= 0:
        print("Principal can't be less than or equal to zero.")

# 3. Input dan Validasi: Rate (Suku Bunga)
# Logika yang sama diterapkan untuk suku bunga: nilainya harus positif.
while rate <= 0:
    rate = float(input("Enter the interest rate: "))

    if rate <= 0:
        print("Interest rate can't be less than or equal to zero.")

# 4. Input dan Validasi: Time (Jangka Waktu)
# Waktu dihitung dalam tahun penuh, sehingga input dikonversi menjadi integer (bilangan bulat).
while time <= 0:
    time = int(input("Enter the time in years: "))

    if time <= 0:
        print("Time can't be less than or equal to zero.")

# 5. Eksekusi Rumus Matematika
# Rumus Bunga Majemuk: A = P(1 + r/n)^(nt)
# Dalam program ini disederhanakan menjadi: total = principal * (1 + rate / 100) ^ time
total = principal * pow((1 + rate / 100), time)

# 6. Menampilkan Hasil (Formatting)
# Mencetak nilai saldo akhir (total) dengan presisi 2 angka di belakang koma menggunakan '.2f'.
print(f"Balance after {time} year/s: ${total:.2f}")

"""
    kita juga bisa menggunakan logika True di sini

    while True:
    if():
    
    else:
    break
    
    dan agar keluar, gunakan nanti break di dalamnya

"""
