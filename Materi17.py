# Program Countdown Timer (Penghitung Waktu Mundur)

import time

# 1. Input Waktu dari Pengguna
# Meminta pengguna memasukkan berapa detik timer akan berjalan.
# Input dikonversi menjadi integer agar bisa digunakan dalam perhitungan matematika.
my_time = int(input("Enter the time in seconds: "))

# 2. Perulangan Menghitung Mundur (For Loop)
# range(start, end, step)
# - start: Dimulai dari angka input (my_time)
# - end: Berakhir di angka 0 (eksklusif, sehingga akan memproses hingga 1)
# - step: -1 artinya menghitung mundur (decrement)
for x in range(my_time, 0, -1):

    # 3. Kalkulasi Waktu (Jam, Menit, Detik)
    # Detik: Sisa bagi (modulus) dari total waktu dibagi 60.
    seconds = x % 60

    # Menit: Membagi total waktu dengan 60 untuk mendapat total menit,
    # lalu di-modulus 60 agar tidak melebihi angka 59.
    minutes = int(x / 60) % 60

    # Jam: Membagi total waktu dengan 3600 (jumlah detik dalam 1 jam).
    hours = int(x / 3600)

    # 4. Format Cetakan Digital
    # Menggunakan f-string dengan padding nol (02) agar angkanya selalu dua digit.
    # Contoh: 9 detik menjadi "09".
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    # 5. Jeda Eksekusi (Sleep)
    # Program "tidur" atau menunda eksekusi selama 1 detik sebelum melanjutkan iterasi berikutnya.
    time.sleep(1)

# 6. Pesan Akhir
# Dicetak setelah perulangan for loop selesai sepenuhnya (waktu habis).
print("TIME'S UP!")


"""
    Manipulasi Fungsi range() untuk Mundur: Trik utama untuk membuat timer adalah membalik arah for loop. Dengan mengatur 
    parameter ketiga pada fungsi range() menjadi -1, iterasi tidak lagi bergerak maju (0, 1, 2...), melainkan menghitung mundur 
    dari nilai my_time menuju angka 0. Ini jauh lebih praktis daripada menggunakan metode pembalikan (reversed method).

    Operasi Modulus (%) untuk Batas Waktu: Jam digital tidak boleh menampilkan angka "65 detik" atau "70 menit". Modulus (% 60) 
    memastikan angka detik dan menit selalu kembali berputar (0-59). Jika nilai sisa bagi dari total detik mencapai kelipatan 
    60, detik akan "direset" kembali menjadi angka kecil, sementara nilai pembagian bulatnya (/ 60) akan diteruskan ke 
    perhitungan menit.

    Pengunci Presisi Waktu (time.sleep()): Loop di dalam Python dapat tereksekusi dalam hitungan milidetik, yang mana terlalu 
    cepat untuk sebuah jam digital. Dengan memanggil utilitas time.sleep(1) dari library bawaan, program dipaksa "membeku" 
    secara akurat selama 1 detik pada tiap putarannya, sehingga sinkron dengan detik di dunia nyata.

    Zero-Padding Formatting (:02): Untuk menjaga estetika format jam digital (seperti 00:05:09 alih-alih 0:5:9), f-string 
    menggunakan flag format specifier :02. Instruksi ini mengalokasikan ruang wajib sebanyak dua karakter, dan akan secara 
    otomatis menyisipkan angka '0' di depan jika nilai waktu tersebut hanya berupa satu digit (di bawah 10).

"""
