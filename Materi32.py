# ==========================================
# 1. KEYWORD ARGUMENTS
# ==========================================
# Positional arguments: Urutan sangat penting.
# Keyword arguments: Menyebutkan nama parameter secara eksplisit saat memanggil fungsi, sehingga urutan tidak lagi penting.

def sapaan_formal(sapaan, gelar, nama_depan, nama_belakang):
    print(f"{sapaan}, {gelar} {nama_depan} {nama_belakang}")

# CONTOH 1: Pemanggilan Standar (Positional Arguments)
# Harus urut: sapaan -> gelar -> nama_depan -> nama_belakang
print("--- Positional Arguments ---")
sapaan_formal("Halo", "Bapak", "Budi", "Santoso")

# CONTOH 2: Pemanggilan dengan Keyword Arguments
# Karena kita menyebutkan nama parameternya, kita bebas mengacak urutannya.
# Ini sangat membantu kejelasan kode saat ada parameter yang mirip.
print("\n--- Keyword Arguments ---")
sapaan_formal(gelar="Bapak", nama_belakang="Santoso", nama_depan="Budi", sapaan="Selamat Pagi")


# ==========================================
# 2. MENGATASI KEBINGUNGAN NAMA
# ==========================================
# Bayangkan Anda memiliki karyawan bernama "James John".
# Apakah nama depannya James, atau John?
print("\n--- Resolusi Ambiguitas ---")
# Tanpa Keyword Args, ini membingungkan saat dibaca oleh programmer lain
sapaan_formal("Welcome", "Mr.", "James", "John")

# Dengan Keyword Args, maksud kode menjadi sangat absolut dan jelas
sapaan_formal(sapaan="Welcome", gelar="Mr.", nama_depan="James", nama_belakang="John")


# ==========================================
# 3. ATURAN PENTING: POSITIONAL HARUS DI DEPAN
# ==========================================
# Jika Anda mencampur Positional Arguments dan Keyword Arguments,
# Semua Positional Arguments HARUS diletakkan di paling depan.

print("\n--- Pencampuran Positional & Keyword ---")
# BENAR: 'Halo' adalah positional (karena di depan), sisanya adalah keyword
sapaan_formal("Halo", nama_belakang="Santoso", gelar="Bapak", nama_depan="Budi")

# SALAH: Ini akan memicu SyntaxError: positional argument follows keyword argument
# sapaan_formal(sapaan="Halo", "Bapak", nama_depan="Budi", nama_belakang="Santoso")


# ==========================================
# 4. IMPLEMENTASI PADA FUNGSI BUILT-IN PYTHON
# ==========================================
print("\n--- Keyword Arguments pada Built-in Function ---")
# Fungsi print() memiliki dua keyword arguments bawaan yang sangat berguna: 'sep' dan 'end'.

# end="": Mengubah karakter akhir (defaultnya ganti baris / \n) menjadi sesuatu yang lain
for x in range(1, 6):
    print(x, end=" ") # Angka dicetak ke samping, bukan ke bawah
print() # Ganti baris

# sep="": Menentukan karakter pemisah jika kita mencetak beberapa variabel sekaligus
print("0812", "3456", "7890", sep="-")

"""
    Membongkar Keterikatan Urutan (Decoupling Position): Dalam fungsi tradisional (Positional Arguments), letak data menentukan 
    identitasnya. Jika parameter pertama adalah nama, maka data pertama yang Anda kirim harus berupa nama. Keyword Arguments 
    memecahkan aturan ini. Dengan mendeklarasikan identitas data secara gamblang saat mengirimnya (misal: nama_depan="Budi"), 
    Python tidak lagi peduli di mana Anda meletakkan data tersebut di dalam keranjang pengiriman. Python akan secara otomatis 
    mencocokkan keyword yang Anda kirim dengan parameter yang memiliki nama yang sama di dalam fungsi [04:10:46].

    Kejelasan Sintaksis (Readability Boost): Manfaat terbesar dari Keyword Arguments bukan sekadar bisa mengacak urutan, 
    melainkan kejelasan. Saat Anda memanggil fungsi yang menerima banyak string atau angka—misalnya get_phone("1", "123", "456", 
    "7890")—programmer lain yang membaca kode tersebut akan kebingungan menebak fungsi dari masing-masing angka. 
    Dengan Keyword Arguments (get_phone(country_code="1", area_code="123", ...), kodenya berubah menjadi dokumentasi yang 
    mendeskripsikan dirinya sendiri.

    Hukum Pencampuran (The Golden Rule of Mixing): Python membebaskan Anda untuk mencampur Positional dan Keyword Arguments 
    dalam satu panggilan fungsi, tetapi dengan satu syarat absolut: Semua Positional Arguments harus diletakkan di depan. 
    Begitu Anda mulai menggunakan Keyword Argument untuk satu data, maka semua data di belakangnya juga wajib menggunakan 
    format Keyword Argument. Jika tidak, Python akan kebingungan mengurai ke mana sisa data yang tidak bernama itu 
    harus dipetakan.
"""