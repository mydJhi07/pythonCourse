# Program Pembuat Persegi Panjang dengan Nested Loop (Perulangan Bersarang)

# 1. Input Dimensi dan Simbol
# Meminta pengguna untuk menentukan panjang baris, kolom, dan simbol yang digunakan.
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

# 2. Outer Loop (Perulangan Luar)
# Mengendalikan jumlah baris (pergerakan vertikal ke bawah).
# Loop ini akan berputar sebanyak nilai 'rows'.
for x in range(rows):

    # 3. Inner Loop (Perulangan Dalam)
    # Mengendalikan jumlah kolom (pergerakan horizontal ke samping).
    # HARUS diselesaikan secara penuh (sebanyak 'columns') sebelum kembali ke Outer Loop.
    # Ingat: Pastikan nama variabel counter berbeda dengan outer loop (misal: 'x' dan 'y').
    for y in range(columns):

        # Mencetak simbol.
        # Parameter end="" mengubah perilaku bawaan print() agar tidak membuat baris baru,
        # sehingga simbol dicetak menyamping secara berdampingan.
        print(symbol, end="")

    # 4. Pemecah Baris (New Line)
    # Setelah Inner Loop selesai mencetak satu baris secara penuh,
    # Outer Loop mengeksekusi print() kosong ini untuk memindahkan kursor ke baris bawahnya.
    print()

"""
    Definisi Perulangan Bersarang (Nested Loop): Konsep ini merujuk pada situasi struktural di mana sebuah blok perulangan 
    ditempatkan di dalam tubuh (kode yang diindentasi) dari perulangan lain. Secara arsitektur, terdapat perulangan luar 
    (outer loop) dan perulangan dalam (inner loop). Tipe perulangan yang dipasangkan sangat situasional dan bisa saling silang 
    (misalnya, for di dalam while, atau sebaliknya).

    Hierarki Eksekusi Total Iterasi: Aturan utama dari nested loop adalah inner loop harus menyelesaikan seluruh siklus putarannya
    hanya untuk memenuhi satu kali siklus putaran dari outer loop. Jika outer loop diatur untuk berjalan 3 kali, dan inner loop
    berjalan 9 kali, maka total eksekusi kode di dalam inner loop adalah 27 iterasi (3 x 9).

    Penggantian Karakter Akhir Baris (end=""): Secara default, fungsi print() di Python selalu mengakhiri cetakan teksnya dengan
    karakter tak kasat mata bernama new line (garis baru). Untuk mencetak simbol secara horizontal untuk membentuk kolom, 
    parameter keyword berupa end="" disuntikkan. Ini akan menimpa pembatas baris baru dengan string kosong atau karakter spasi,
    memaksa teks selanjutnya untuk menempel di samping teks sebelumnya.

    Pembentukan Grid/Matriks: Kombinasi outer dan inner loop sangat ideal untuk membangun grid dua dimensi. Inner loop bertugas
    merender elemen secara menyamping (kolom). Begitu satu kolom selesai dirender, eksekusi kembali ke outer loop yang memanggil
    fungsi print() kosong. Fungsi kosong ini bertindak sebagai pemutus baris yang mengembalikan kursor ke bawah untuk memulai
    proses render baris yang baru, menghasilkan bentuk persegi atau matriks.

"""
