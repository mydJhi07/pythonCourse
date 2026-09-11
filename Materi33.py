# ==========================================
# 1. *ARGS (Arbitrary Positional Arguments)
# ==========================================
# Mengizinkan fungsi menerima jumlah argumen posisional yang tidak terbatas.
# Parameter dengan awalan * akan mengemas (pack) semua argumen ke dalam bentuk TUPLE.

def hitung_total(*args):
    # 'args' sekarang adalah sebuah Tuple, contoh: (1, 2, 3, 4, 5)
    total = 0
    for angka in args:
        total += angka
    return total

print("--- Hasil *args ---")
print("Total 3 angka:", hitung_total(1, 2, 3))
print("Total 6 angka:", hitung_total(1, 2, 3, 4, 5, 6))


# ==========================================
# 2. **KWARGS (Arbitrary Keyword Arguments)
# ==========================================
# Mengizinkan fungsi menerima jumlah argumen keyword yang tidak terbatas.
# Parameter dengan awalan ** akan mengemas (pack) argumen ke dalam bentuk DICTIONARY.

def cetak_alamat(**kwargs):
    # 'kwargs' sekarang adalah sebuah Dictionary, 
    # contoh: {'jalan': 'Jl. Merdeka', 'kota': 'Jakarta'}
    print("\n--- Hasil **kwargs ---")
    for kunci, nilai in kwargs.items():
        print(f"{kunci.capitalize()}: {nilai}")

# Bebas memasukkan berapa pun jumlah keyword arguments
cetak_alamat(jalan="Jl. Sudirman", kota="Jakarta", kode_pos="12345")
cetak_alamat(jalan="Jl. Asia Afrika", kota="Bandung", provinsi="Jawa Barat", negara="Indonesia")


# ==========================================
# 3. MENGGABUNGKAN *ARGS DAN **KWARGS
# ==========================================
# ATURAN EMAS: *args HARUS diletakkan sebelum **kwargs di dalam parameter fungsi.

def cetak_label_pengiriman(*args, **kwargs):
    print("\n--- Label Pengiriman Resmi ---")
    
    # 1. Memproses *args (Sebagai Nama/Gelar)
    for arg in args:
        print(arg, end=" ")
    print() # Pindah baris
    
    # 2. Memproses **kwargs (Sebagai Detail Alamat)
    # Menggunakan metode .get() dari dictionary agar tidak error jika data kosong
    print(f"{kwargs.get('jalan', 'Jalan tidak diketahui')}")
    print(f"{kwargs.get('kota', 'Kota tidak diketahui')}, {kwargs.get('provinsi', '')}")
    
    # Pengecekan data opsional
    if 'apartemen' in kwargs:
        print(f"Apt No: {kwargs.get('apartemen')}")

# Argumen posisional diletakkan di depan, diikuti argumen keyword di belakang
cetak_label_pengiriman("Dr.", "Alan", "Turing", jalan="Bletchley Park", kota="Milton Keynes", apartemen="Hut 8")

"""
    Mengatasi Batasan Parameter Fix (Arbitrary Arguments): Pada fungsi Python biasa, jika Anda menetapkan 2 parameter, Anda 
    wajib mengirim tepat 2 argumen. Namun, di dunia nyata, data sering kali dinamis (misalnya fungsi untuk menjumlahkan 
    sekumpulan angka di mana jumlah angkanya bisa 2, 5, atau 100). Parameter *args dan **kwargs memecahkan masalah ini dengan 
    menerima jumlah argumen yang "sewenang-wenang" (arbitrary / tidak terbatas).

    Rahasia Unpacking Operator (* dan **): Bagian ajaibnya bukanlah pada kata "args" atau "kwargs" (Anda bebas menamainya *angka 
    atau **data), melainkan pada simbol bintangnya (asterisk).

        Simbol * tunggal akan menyapu semua positional argument yang tersisa dan memampatkannya (pack) menjadi satu struktur data
        Tuple.

        Simbol ** ganda akan menyapu semua keyword argument (seperti jalan="Melati") dan memampatkannya menjadi struktur data 
        Dictionary (Key-Value Pairs).

    Fleksibilitas Manipulasi Data: Karena *args berubah menjadi Tuple dan **kwargs berubah menjadi Dictionary di dalam fungsi, 
    Anda bisa menggunakan seluruh metode bawaan dari kedua tipe data tersebut. Anda bisa menggunakan perulangan for pada Tuple 
    untuk menghitung nilai, atau menggunakan .get(), .items(), .keys(), dan .values() pada Dictionary untuk mengelola detail 
    kompleks seperti alamat atau profil pengguna.

    Hukum Hierarki Sintaksis (Positional Before Keyword): Jika Anda merancang fungsi tingkat lanjut yang menggabungkan 
    keduanya—seperti def fungsi_kompleks(*args, **kwargs):—aturan mainnya mutlak: argumen posisional (*args) harus selalu masuk 
    lebih dulu sebelum argumen keyword (**kwargs). Python akan kebingungan membaca alur datanya jika Anda membalik urutannya dan 
    akan langsung memberikan SyntaxError.
"""