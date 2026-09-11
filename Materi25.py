# Program Concession Stand (Kasir Bioskop)

# 1. Menu dideklarasikan sebagai Dictionary
# Key adalah nama makanan/minuman (string), Value adalah harganya (float).
menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

# 2. Deklarasi Keranjang dan Total
cart = []
total = 0

# 3. Menampilkan Menu Menggunakan Looping
print("--------- MENU ---------")
# .items() mengurai dictionary menjadi sepasang (key, value)
for key, value in menu.items():
    # Pemformatan string:
    # {key:10} memberikan alokasi ruang 10 karakter untuk mensejajarkan harga.
    # {value:.2f} memastikan harga dicetak dengan 2 angka di belakang koma (format mata uang).
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

# 4. Interaksi Pembelian dengan While Loop
while True:
    # Menerima input dari pengguna dan mengubahnya ke huruf kecil untuk konsistensi
    food = input("Select an item (q to quit): ").lower()
    
    if food == "q":
        # Jika pengguna menekan 'q', hentikan perulangan (escape loop)
        break
    elif menu.get(food) is not None:
        # Jika barang ditemukan di dalam menu (hasilnya BUKAN None),
        # masukkan barang tersebut ke dalam list 'cart'.
        cart.append(food)
    else:
        # Menangani input yang salah atau barang tidak tersedia
        print(f"Sorry, '{food}' is not on the menu.")

# 5. Menampilkan Struk dan Kalkulasi Total
print("\n------ YOUR ORDER ------")
# Iterasi melalui setiap makanan yang ada di keranjang belanja
for food in cart:
    # Mencetak makanan ke layar (horizontal)
    print(food, end=" ")
    
    # Mencari harga dari makanan tersebut di 'menu', lalu menjumlahkannya ke 'total'
    total += menu.get(food)

print() # Baris baru untuk jarak visual
print(f"Total is: ${total:.2f}")
print("------------------------")

"""
    Arsitektur Dictionary: Program ini memodelkan papan menu kasir (Concession Stand) menggunakan struktur Dictionary. Hal ini
    sangat ideal karena kita perlu memetakan label item (seperti "popcorn") langsung ke harga spesifiknya ($6.00). Dictionary 
    memungkinkan program untuk melakukan pencarian harga seketika tanpa harus melakukan iterasi panjang ke seluruh sistem.

    Pemformatan UI Kasir: Untuk mencetak menu, method .items() dimanfaatkan untuk mengekstrak baik key maupun value. Menariknya,
    formatting khusus {key:10} ditambahkan pada cetakan f-string. Angka 10 ini berfungsi memberikan alokasi ruang tetap sebanyak 
    10 karakter pada layar konsol untuk kolom nama barang. Ini mencegah harga menjadi berantakan (tidak sejajar vertikal) akibat 
    perbedaan panjang kata "pizza" dan "lemonade".

    Sistem Validasi dan Akuisisi (.get): Ketika while loop menerima input pesanan pengguna, ia tidak secara serampangan 
    memasukkannya ke dalam list keranjang (cart). Ia akan memanggil menu.get(food). Jika pengguna mengetik "potato" 
    (tidak ada di menu), get() tidak akan menyebabkan error, melainkan diam-diam merespons dengan None. Kondisi elif 
    menangkap momen ini; item hanya diizinkan masuk ke keranjang (cart.append) jika respons dari .get() bukanlah None.

    Eksekusi Kalkulasi Akhir: Pada fase penyelesaian (checkout), loop akan memeriksa seluruh barang yang terlanjur terdaftar di 
    list keranjang (cart). Di sinilah efisiensi Dictionary terasa. Daripada membuat percabangan if-else yang sangat panjang 
    (jika barang = pizza tambah $3, jika nachos tambah $4.50), program ini cukup menembak fungsi kalkulasi total dengan perintah 
    total += menu.get(food). Fungsi tersebut akan menarik harga yang terkunci di dalam kamus, menjumlahkannya ke total 
    akhir secara otomatis berulang-ulang hingga daftar keranjang habis.
"""