price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 3000000.12

# 1. Presisi Desimal (.2f)
# - Mengontrol jumlah angka di belakang koma untuk bilangan desimal (float).
# - '.2f' berarti menampilkan 2 digit di belakang koma.
print(f"Presisi: ${price1:.2f}")

# 2. Alokasi Ruang / Lebar Karakter (10)
# - Menentukan total karakter ruang yang disediakan (dalam hal ini 10 karakter).
print(f"Ruang: ${price2:10}")

# 3. Padding Nol (010)
# - Mengisi ruang kosong (padding) dengan angka '0' di depan nilai, bukan spasi kosong.
print(f"Padding: ${price3:010}")

# 4. Justifikasi: Kiri (<), Kanan (>), dan Tengah (^)
# - Mengatur perataan teks/angka dalam ruang yang sudah dialokasikan.
print(f"Kiri   : ${price1:<10}")
print(f"Kanan  : ${price2:>10}")
print(f"Tengah : ${price3:^10}")

# 5. Penanda Tanda Positif (+) dan Spasi Kosong ( )
# - Memaksa simbol positif '+' tampil untuk angka yang bernilai positif.
# - Spasi kosong memberikan jarak agar angka positif bisa sejajar lurus dengan tanda minus di angka negatif.
print(f"Plus   : ${price1:+}")
print(f"Spasi  : ${price3: }")

# 6. Pemisah Ribuan (,)
# - Menambahkan tanda koma (,) untuk setiap kelipatan ribuan agar angka besar mudah dibaca.
print(f"Ribuan : ${price4:,}")

# 7. Kombinasi Format (+,.2f)
# - Menggabungkan beberapa flag sekaligus.
# - Pada contoh ini: tanda positif (+), pemisah ribuan (,), dan presisi 2 desimal (.2f).
print(f"Kombinasi: ${price4:+,.2f}")

"""
    Format Specifiers dalam f-string: Di dalam Python, format specifiers memungkinkan kontrol penuh atas bagaimana suatu nilai 
    ditampilkan ke layar. Utilitas ini diaktifkan di dalam placeholder sebuah f-string dengan menambahkan titik dua (:) setelah 
    nama variabel, yang kemudian diikuti oleh berbagai flags pengaturan format.

    Presisi Desimal (.Nf): Digunakan secara spesifik untuk memotong atau membulatkan angka float. Sebagai contoh, .2f memastikan 
    bahwa angka tersebut selalu dikunci untuk hanya menampilkan dua digit setelah titik desimal, membuang atau menyembunyikan 
    sisa digit yang ada.

    Alokasi Lebar Karakter: Dengan memberikan angka bulat (seperti 10) setelah titik dua, program akan memesan memori visual 
    sebanyak 10 karakter ruang. Jika nilai angka aslinya kurang dari 10 karakter, maka sisa tempat tersebut akan dibiarkan 
    sebagai spasi kosong.

    Zero Padding: Mengombinasikan karakter 0 di depan angka alokasi ruang (contoh: 010) akan mengubah cara program mengisi 
    kekosongan. Alih-alih merender spasi kosong, sisa karakter tersebut akan diisi penuh dengan angka nol.

    Pengaturan Justifikasi (<, >, ^): Berfungsi jika ada alokasi karakter yang lebih lebar dari angka aslinya. Flag < akan 
    meratakan nilai ke sisi paling kiri, > akan memaksanya ke kanan (merupakan posisi default untuk angka), dan ^ 
    menempatkan karakter presisi di tengah-tengah ruang.

    Penanganan Simbol Numerik (+ / spasi): Secara bawaan, Python hanya mencetak tanda minus (-) untuk angka negatif dan 
    menyembunyikan tanda plus. Dengan memberikan flag +, program dipaksa untuk selalu memunculkan tanda positif. Sebagai 
    alternatif, memberikan flag spasi ( ) akan menyuntikkan satu karakter spasi pada cetakan angka positif agar dapat sejajar 
    secara vertikal dengan simbol minus pada angka negatif.

    Pemisah Ribuan (,): Menambahkan flag koma (,) merupakan metode instan untuk menyisipkan pemisah antar blok kelipatan ribu 
    pada deret bilangan, mempermudah pembacaan pada format angka yang besar.

    Manipulasi Kompleks (Kombinasi Flags): Seluruh flags tersebut tidak bersifat kaku atau tunggal. Mereka dapat dirangkai dan 
    dikombinasikan bersamaan (seperti +,.2f yang secara berurutan mengeksekusi tanda positif, koma ribuan, dan potongan dua 
    desimal) untuk mencapai standar pemformatan yang sangat rinci.

"""
