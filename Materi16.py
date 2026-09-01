# 1. Dasar For Loop dengan range()
# Mengeksekusi blok kode dalam jumlah putaran yang pasti (fixed number of times).
# range(startIndex, endIndex): endIndex bersifat eksklusif (tidak termasuk).
# Contoh: Menghitung 1 sampai 10 (maka endIndex diatur ke 11).
for x in range(1, 11):
    print(x)

# 2. Menghitung Mundur dengan reversed()
# Membalikkan arah eksekusi dari fungsi range().
# Contoh: Menghitung mundur dari 10 ke 1.
for x in reversed(range(1, 11)):
    print(x)
    print("Happy New Year!")

# 3. Menghitung dengan Langkah Tertentu (Step)
# Argumen ketiga pada range() menetapkan seberapa jauh jarak/lompatan tiap iterasi.
# Contoh: Mencetak angka dengan jarak 2 langkah (menghasilkan angka ganjil 1, 3, 5, 7, 9).
for x in range(1, 11, 2):
    print(x)

# 4. Iterasi pada Objek Teks (String)
# For loop tidak hanya untuk angka, melainkan berlaku pada semua tipe data 'iterable'.
# Program akan membaca dan membedah string per satu karakter secara berurutan.
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

# 5. Mengendalikan Alur Iterasi: 'continue' dan 'break'
# Menggunakan if statement untuk mengintervensi laju loop di tengah jalan.
for x in range(1, 21):
    if x == 13:
        # continue: Membatalkan sisa kode di putaran ini, lalu melompat langsung ke putaran berikutnya.
        # Angka 13 akan diabaikan/skip.
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        # break: Menghentikan paksa dan menghancurkan seluruh perulangan secara total.
        # Loop berhenti murni saat mencapai angka 13.
        break
    else:
        print(x)

"""
    Perulangan Terbatas (Fixed Iteration): Berbeda dari while loop yang perulangannya bergantung pada evaluasi kondisi 
    benar/salah secara dinamis, for loop digunakan ketika programmer sudah mengetahui dengan pasti seberapa banyak eksekusi 
    kode harus dilakukan. Loop ini didesain untuk menelusuri segala sesuatu yang berstatus iterable (dapat diurai), seperti 
    rentang angka, string, atau urutan data.

    Logika Fungsi range(start, end, step): Fungsi range() mendikte lintasan iterasi. Argumen kedua (end) selalu dibaca secara 
    eksklusif oleh Python. Artinya, jika Anda ingin menghitung sampai 10, Anda harus menulis batasnya hingga 11 (range(1, 11)). 
    Argumen ketiga yang opsional (step) bisa disisipkan jika program harus mengabaikan urutan default dan menghitung dengan 
    kelipatan tertentu, misal kelipatan 2 atau 3.

    Inversi Otomatis (reversed): Untuk menghasilkan hitungan mundur, programmer tidak perlu merombak arah iterasi angka dengan 
    kalkulasi matematika pengurangan secara manual. Fungsi utilitas bawaan reversed() dapat membungkus range tersebut dan 
    langsung memutar balik urutan eksekusi objek iterable di dalamnya.

    Sifat Unversal (Membaca String): Kemampuan for loop meluas pada objek yang terbuat dari sekumpulan data. Saat mengevaluasi 
    variabel string (seperti tulisan "1234-5678..."), loop memperlakukan string tersebut sebagai deretan karakter, lalu 
    mengisolasi dan memproses satu persatu huruf atau simbol dari kiri ke kanan.

    Intervensi Alur (continue & break): Python menyediakan dua kata kunci pengaman jika harus menyela putaran loop akibat 
    kondisi tertentu. Perintah continue bertugas "melewati" sisa kode pada putaran saat itu (misalnya: saat putaran mencapai 
    angka 13, sisa perintah di bawahnya diabaikan) dan seketika langsung kembali ke puncak untuk putaran ke-14. Sedangkan 
    perintah break berfungsi seperti rem darurat; kata kunci ini akan memutus, membatalkan, dan memaksa program keluar 
    sepenuhnya dari belenggu for loop tersebut.

"""
