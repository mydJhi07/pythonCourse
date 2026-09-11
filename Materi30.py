# ==========================================
# 1. FUNGSI DASAR (Tanpa Parameter)
# ==========================================
# Gunakan keyword 'def' (define) diikuti nama fungsi dan tanda kurung ().
def happy_birthday():
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday dear you!")
    print("Happy birthday to you!\n")

# Cara memanggil (invoke) fungsi:
happy_birthday()
happy_birthday() # Dipanggil berkali-kali tanpa harus menulis ulang kodenya


# ==========================================
# 2. FUNGSI DENGAN PARAMETER & ARGUMEN
# ==========================================
# Fungsi ini meminta 3 data (parameter) untuk bisa bekerja.
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

# Mengirimkan data nyata (argumen) ke dalam fungsi. 
# Urutan pengiriman (posisi) harus persis sama dengan parameter.
display_invoice("BroCode", 42.50, "Jan 1st")


# ==========================================
# 3. FUNGSI DENGAN RETURN (Mengembalikan Nilai)
# ==========================================
def add(x, y):
    z = x + y
    return z  # Melemparkan nilai z kembali ke si pemanggil (caller)

def subtract(x, y):
    return x - y # Versi lebih singkat

# Karena fungsi 'add' mengembalikan nilai, kita bisa menyimpannya ke dalam variabel
result = add(1, 2)
print(f"The addition result is: {result}")


# ==========================================
# 4. CONTOH KOMPLEKS: Manipulasi Teks + Return
# ==========================================
def create_name(first, last):
    # Memanipulasi data yang masuk
    first = first.capitalize()
    last = last.capitalize()
    
    # Mengembalikan hasil gabungan
    return first + " " + last

# Pemanggilan fungsi dan menyimpan hasilnya
full_name = create_name("spongebob", "squarepants")
print(full_name) # Output: Spongebob Squarepants

"""
    Sintaks def dan Invocation (Pemanggilan): Untuk membuat fungsi, Anda selalu memulainya dengan kata kunci def, nama fungsi, 
    titik dua :, lalu menuliskan instruksi yang di-indentasi (menjorok ke dalam) di bawahnya. Fungsi ini akan diam saja sampai 
    Anda memanggilnya (invoke). Menganalogikan tanda kurung () saat memanggil fungsi, anggap saja itu seperti mengangkat gagang 
    telepon untuk memanggil fungsi tersebut agar mulai bekerja.
    
    Parameter vs Argumen: Ini adalah jembatan komunikasi data. Parameter (seperti username, amount di fungsi display_invoice) 
    adalah nama variabel sementara yang bertugas menangkap data di pintu masuk fungsi. Argumen adalah data aktual yang Anda 
    lempar ke dalam tanda kurung saat memanggil fungsi tersebut (misal: "BroCode", 42.50). Hukum mutlaknya: Urutan posisi 
    argumen yang Anda kirim harus sama persis dengan urutan parameter yang diminta, jika tidak data akan tertukar.

    Peran Vital return: Jika perintah print() hanya sekadar menampilkan teks ke layar monitor, perintah return adalah jantung 
    dari fungsi operasional. return bertugas menghentikan eksekusi di dalam fungsi secara instan, lalu "melemparkan" hasil 
    perhitungan atau manipulasi data tersebut kembali ke titik di mana fungsi itu dipanggil. Oleh karena itu, kita bisa 
    menyimpan hasil dari add(1, 2) ke dalam variabel result, karena fungsi tersebut mengembalikan sebuah barang (angka 3) ke 
    tangan kita.
"""