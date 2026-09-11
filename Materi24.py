# 1. Deklarasi Dictionary (Koleksi Pasangan Key-Value)
# Dictionary dibuat menggunakan kurung kurawal {} dengan format 'key': 'value'.
# Key berfungsi seperti "indeks label" khusus yang harus unik (tidak boleh duplikat).
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# 2. Mengakses Nilai Secara Aman (.get)
# Daripada menggunakan kurung siku (capitals["Japan"]) yang akan memicu fatal error jika data tidak ada,
# metode .get() jauh lebih aman karena akan mengembalikan 'None' jika key tidak ditemukan.
print(capitals.get("USA")) # Output: Washington D.C.

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist") # Karena Japan tidak ada, ini yang dieksekusi

# 3. Menambahkan atau Mengubah Data (.update)
# Memasukkan dictionary baru ke dalam dictionary yang sudah ada.
# Jika key belum ada, data akan disisipkan. Jika key sudah ada, nilainya akan ditimpa (di-update).
capitals.update({"Germany": "Berlin"}) # Menyisipkan data baru
capitals.update({"USA": "Detroit"})    # Menimpa nilai dari key "USA" yang sudah ada

# 4. Menghapus Data (.pop, .popitem, .clear)
capitals.pop("China")    # Mencari dan menghapus pasangan secara presisi berdasarkan nama 'key'
capitals.popitem()       # Menghapus pasangan key-value yang berada di urutan paling akhir / terbaru
# capitals.clear()       # (Hati-hati) Menghancurkan dan mengosongkan seluruh isi dictionary

# 5. Ekstraksi dan Iterasi Data (.keys, .values, .items)
# A. Ekstraksi khusus Kunci (Keys)
print("\n--- Keys ---")
for key in capitals.keys():
    print(key)

# B. Ekstraksi khusus Nilai (Values)
print("\n--- Values ---")
for value in capitals.values():
    print(value)

# C. Ekstraksi Lengkap (Key-Value Pairs)
# .items() memecah isi dictionary menjadi sepasang data (Tuple) pada tiap iterasinya.
# Oleh karena itu, kita membutuhkan DUA variabel di dalam for loop (key, value).
print("\n--- Items (Key-Value) ---")
for key, value in capitals.items():
    print(f"{key} : {value}")

"""
    Arsitektur Key-Value Pairs: Dictionary adalah salah satu collection paling krusial di Python karena kemampuannya memetakan 
    data dengan label. Jika pada List Anda harus mengingat bahwa angka 3.14 ada di indeks [0], di dalam Dictionary Anda bisa 
    memanggilnya menggunakan kata kunci deskriptif yang logis, seperti nama negara untuk memanggil nama ibukotanya. Aturan
    mutlaknya adalah: Keys (kunci) tidak boleh ada yang duplikat, sedangkan Values (nilai) boleh berulang.

    Keamanan Ekstraksi dengan get(): Pendekatan standar dalam memanggil nilai dictionary biasanya memicu masalah jika kunci 
    yang dicari ternyata tidak eksis (program akan crash). Metode .get() diciptakan untuk mitigasi tersebut. Ketika 
    .get("Japan") dipanggil dan sistem gagal menemukannya, ia tidak akan memutus program dengan Error, melainkan merespons 
    secara senyap dengan objek hampa None yang bisa ditangkap oleh blok evaluasi if-else.

    Pembaruan Fleksibel dengan update(): Fungsi .update() memiliki perilaku hibrida. Ia membaca dictionary yang disuntikkan 
    kepadanya, lalu mengevaluasinya. Jika kunci tersebut benar-benar entitas baru, ia akan memanjangkan dictionary asal. 
    Namun, karena hukum dictionary menolak duplikasi kunci, jika Anda menggunakan .update() pada kunci yang sudah ada, ia 
    akan menimpa dan memodifikasi nilainya secara langsung.

    Metode Pembongkaran Beragam Dimensi (keys, values, items): Dictionary adalah struktur yang kompleks, sehingga Python 
    menyediakan tiga lapis cara untuk membongkarnya di dalam loop. .keys() digunakan jika Anda hanya peduli pada indeks 
    labelnya. .values() digunakan jika Anda hanya peduli pada data mentahnya tanpa perlu tahu labelnya. Metode yang paling 
    sering digunakan, .items(), membongkar struktur tersebut sehingga loop akan terus-menerus disuapi dua variabel secara 
    sinkron (kunci dan nilai) untuk dicetak secara bersamaan pada f-string.
"""