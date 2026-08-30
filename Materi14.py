# 1. Konsep Dasar While Loop: Perulangan selama kondisi True
# Program akan terus meminta input nama hingga pengguna benar-benar mengetikkan sesuatu.
# Kondisi ini menahan eksekusi program selanjutnya sampai syarat terpenuhi.
name = ""
while name == "":
    name = input("Enter your name: ")
    if name == "":
        print("You did not enter your name")

print(f"Hello {name}")

# 2. Infinite Loop & Escape Strategy (Strategi Keluar)
# Memastikan pengguna memasukkan angka yang valid (antara 1 hingga 10).
# Menggunakan operator logika 'or' untuk mengecek apakah angka di luar batas.
num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")

    # STRATEGI KELUAR: Meminta input ulang di dalam blok perulangan.
    # Jika baris ini tidak ada, program akan terjebak mencetak teks selamanya (Infinite Loop).
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}")

# 3. Kondisi Terbalik dengan Operator Logika (not)
# Loop berjalan selama input yang diberikan BUKAN karakter 'q' (Quit).
food = input("Enter a food you like (q to quit): ")

while not food.lower() == "q":
    print(f"You like {food}")

    # Meminta input baru agar kondisi while bisa dievaluasi kembali di putaran berikutnya.
    food = input("Enter another food you like (q to quit): ")

print("bye")

"""
    Eksekusi Berkelanjutan (While Condition): Berbeda dengan if statement yang hanya mengeksekusi blok kode satu kali jika 
    kondisi terpenuhi, while loop akan terus mengeksekusi blok kode secara berulang-ulang selama kondisi yang dievaluasinya 
    tetap bernilai True. Konsep ini sangat ideal untuk memvalidasi input pengguna, di mana program secara konstan "mengunci" 
    pengguna di satu tahap hingga mereka memberikan data yang valid.

    Risiko Infinite Loop & Escape Strategy: Kelemahan utama dari while loop adalah risiko terjadinya perulangan tanpa henti 
    (infinite loop). Hal ini terjadi apabila kondisi pemicu perulangan selalu True dan tidak ada modifikasi di dalam bloknya. 
    Oleh karena itu, wajib bagi programmer untuk menyediakan escape strategy—biasanya dengan cara meminta ulang input atau 
    memodifikasi variabel pemicu di dalam tubuh loop—sehingga sewaktu-waktu kondisi dapat berubah menjadi False dan perulangan 
    berakhir.

    Kombinasi Logika Ekstensif (or & not): while loop sangat kuat jika dipadukan dengan operator logika. Menggunakan or, program
    dapat menahan pengguna jika input mereka jatuh di rentang bawah atau atas (misalnya, angka di bawah 1 ATAU di atas 10). Di
    sisi lain, operator not membalikkan logika normal, menginstruksikan loop untuk terus berjalan "selama inputnya bukan tombol
    pembatalan (seperti tombol 'q')", yang sering diaplikasikan pada menu interaktif atau permainan.


"""
