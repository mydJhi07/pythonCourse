# Program Keranjang Belanja Sederhana

# 1. Deklarasi Struktur Data Utama
# Kita menggunakan list karena data keranjang belanja sifatnya fleksibel (bisa bertambah), 
# berurutan, dan memungkinan duplikasi (membeli barang yang sama berkali-kali).
foods = []
prices = []
total = 0

# 2. Perulangan Interaktif (Input Barang)
# while True: Menciptakan perulangan yang akan terus berjalan hingga diputus secara manual (break).
while True:
    food = input("Enter a food to buy (q to quit): ")
    
    # Escape Strategy: Jika pengguna mengetik 'q' atau 'Q', keluar dari loop.
    # lower() digunakan agar program tidak case-sensitive (mengenali 'q' maupun 'Q').
    if food.lower() == "q":
        break
    else:
        # Menambahkan barang ke dalam list makanan
        foods.append(food)
        
        # Meminta input harga. Tipe data di-cast menjadi float untuk mengakomodasi angka desimal.
        price = float(input(f"Enter the price of {food}: $"))
        
        # Menambahkan harga ke dalam list harga
        prices.append(price)

# 3. Menampilkan Isi Keranjang
print("\n----- YOUR CART -----")
# Iterasi melalui setiap makanan yang ada di dalam list foods
for food in foods:
    # end=" " memastikan setiap makanan dicetak menyamping secara berdampingan, bukan baris baru.
    print(food, end=", ")

# 4. Kalkulasi Total Harga
# Iterasi melalui setiap nominal yang ada di dalam list prices
for price in prices:
    # Memperbarui nilai total dengan menambahkan harga saat ini ke total sebelumnya.
    # total += price adalah penulisan singkat dari total = total + price.
    total += price

# Mencetak baris baru yang kosong sebagai pembatas visual
print() 

# 5. Menampilkan Total Harga (Formatting)
# Menampilkan total yang harus dibayar, dikunci pada presisi dua angka desimal (.2f)
print(f"Your total is: ${total:.2f}")

"""
    Pemilihan Struktur Data (Lists): Program ini menggunakan dua buah List kosong (foods dan prices) pada tahap awal.
    Mengapa tidak menggunakan Tuples atau Sets? Tuples bersifat immutable (tidak bisa ditambah isi), sedangkan Sets tidak 
    memiliki urutan yang jelas. List dipilih karena ia bisa terus menampung data baru, mempertahankan urutan masuk, dan 
    mengizinkan duplikasi pembelian.

    Infinite Loop untuk Interaksi Berkelanjutan: Agar aplikasi kasir tidak langsung mati setelah pengguna memasukkan satu 
    barang, digunakan konstruksi while True. Ini memaksa sistem untuk terus menagih input barang secara konstan. Loop ini hanya
    akan dihancurkan oleh perintah break manakala user mengetik instruksi khusus, yaitu huruf 'q'.

    Normalisasi Input Kasus (lower()): Pengguna bisa saja tidak sengaja mengetik huruf kapital 'Q'. Agar sistem tetap mengenali
    instruksi tersebut, food.lower() dipanggil sesaat sebelum evaluasi if, sehingga apa pun bentuk ketikannya, Python akan 
    membacanya sebagai huruf kecil murni ('q').

    Penambahan Data Dinamis (append()): Jika input lulus filter (bukan 'q'), program akan menyuntikkan data nama makanan ke 
    dalam ujung list foods melalui fungsi bawaan append(). Langkah serupa kemudian dilakukan untuk mengakuisisi harganya, yang
    langsung dikonversi ke float (desimal) lalu dimasukkan ke dalam keranjang prices.

    Proses Kalkulasi (Accumulation): Tahap akhir dari program adalah menjumlahkan seluruh harga. For loop bertugas membedah 
    keranjang prices satu per satu. Operator majemuk += memegang peran kunci di sini; ia akan terus mengakumulasikan nominal 
    harga yang sedang disorot loop ke dalam brankas variabel penampung total, hingga seluruh isi list tuntas dihitung =.
"""