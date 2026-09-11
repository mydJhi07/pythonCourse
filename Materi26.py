import random

# ==========================================
#   PENGGUNAAN DASAR MODUL RANDOM
# ==========================================

# A. Menghasilkan Angka Bulat Acak (Integer)
# randint(min, max) menghasilkan angka bulat antara nilai min dan max (inklusif).
# Sering digunakan untuk simulasi dadu atau pilihan acak terikat angka.
angka_dadu = random.randint(1, 6)
print(f"Hasil lemparan dadu: {angka_dadu}")

# B. Menghasilkan Angka Desimal Acak (Float)
# random() menghasilkan angka desimal murni di antara 0.0 hingga (sebelum) 1.0.
# Sangat krusial untuk simulasi persentase atau sistem drop-rate game.
angka_desimal = random.random()
print(f"Angka desimal acak: {angka_desimal:.2f}")

# C. Memilih Item Acak dari Koleksi (List/Tuple)
# choice() memilih satu elemen secara acak dari dalam urutan yang diberikan.
opsi = ("batu", "gunting", "kertas")
pilihan_komputer = random.choice(opsi)
print(f"Komputer memilih: {pilihan_komputer}")

# D. Mengacak Urutan Koleksi (Shuffle)
# shuffle() akan memodifikasi list asli dan mengacak posisinya. Hanya bekerja pada List (karena Tuples statis).
kartu = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(kartu)
print(f"Susunan kartu setelah dikocok: {kartu[:5]} ...")


"""
    Impor Mutlak random: Python tidak secara bawawaan memuat fungsionalitas pengacakan angka pada runtime dasarnya untuk 
    menghemat memori. Oleh karena itu, kita wajib mendeklarasikan instruksi import random di paling atas skrip sebelum memanggil
    fungsi seperti randint atau choice.

    Perbedaan Esensial randint dan random: Kapan menggunakan yang mana? Jika Anda mensimulasikan sistem bertahap diskrit 
    (Dadu sisi 20, memilih nomor urut absen 1-100), gunakan random.randint(min, max) yang menghasilkan angka bulat utuh. 
    Namun, jika Anda berhadapan dengan probabilitas, peluang cuaca, atau kecepatan objek, random.random() yang memproduksi angka 
    desimal dari $0.0$ hingga $0.999$ adalah pilihan yang tepat secara matematis.

    Utilitas Koleksi (choice & shuffle): Modul random juga menyediakan dua metode mematikan untuk collection. Metode choice()
    bisa menganalisis sebuah Tuple atau List berisi nama-nama, lalu memilih satu secara acak. Sangat cocok untuk mekanisme 
    drop-loot atau bot AI yang memilih batu/gunting/kertas. Metode shuffle(), di sisi lain, secara fisik mengacak urutan dari 
    sebuah List layaknya mengocok dek kartu remi. Ingat, shuffle() akan memicu Error jika diterapkan pada Tuple karena
    sifatnya yang terkunci.

    Benteng Validasi (isdigit()): Pada baris kode tebak angka, tantangan terbesarnya adalah User Error. Ketika program meminta 
    angka $1-100$, user bisa saja usil mengetikkan kata "pizza". Jika Python mencoba mengubah teks "pizza" menjadi int(), 
    program akan mati konyol (Crash: ValueError). Evaluasi protektif if not tebakan.isdigit(): menjadi perisai utama. Ia 
    memverifikasi apakah string input benar-benar hanya berisi karakter numerik sebelum diolah menjadi matematika murni.
"""