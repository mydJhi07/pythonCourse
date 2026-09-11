import time

# ==========================================
# 1. FUNGSI DENGAN DEFAULT ARGUMENT
# ==========================================
# Parameter 'discount' dan 'tax' diberikan nilai bawaan.
# Jika saat pemanggilan data ini tidak dikirim (omitted), nilai 0 dan 0.05 akan dipakai.
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# Skenario 1: Hanya mengirim 1 argumen (list_price). 
# discount otomatis 0, dan tax otomatis 0.05 (5%).
print(f"Harga normal: ${net_price(500):.2f}") 

# Skenario 2: Mengirim 2 argumen. 
# list_price=500, discount=0.1 (Diskon 10%). tax tetap default 0.05.
print(f"Harga diskon 10%: ${net_price(500, 0.1):.2f}")

# Skenario 3: Mengirim 3 argumen. 
# Nilai default akan sepenuhnya ditimpa (overwrite) oleh nilai baru ini.
print(f"Harga tanpa pajak: ${net_price(500, 0.1, 0):.2f}")


# ==========================================
# 2. ATURAN POSISI DEFAULT ARGUMENT
# ==========================================
# ATURAN EMAS: Parameter dengan nilai default (start=0) HARUS diletakkan 
# di belakang (setelah) parameter biasa (end) yang tidak memiliki nilai default.
# Contoh SALAH: def count(start=0, end): -> Memicu SyntaxError

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1) # Jeda 1 detik
    print("DONE!")

print("\n--- Mulai Menghitung ---")
# Pemanggilan dengan 1 argumen: 'end' menjadi 5, 'start' tetap 0
count(5) 

print("\n--- Menghitung dengan Start Baru ---")
# Pemanggilan dengan 2 argumen: 'end' menjadi 10, 'start' ditimpa menjadi 7
count(10, 7)

"""
    Fleksibilitas Pemanggilan Fungsi: Default argument memberikan opsi kepada pemanggil fungsi (caller). Anda bisa memanggil 
    fungsi net_price dengan 1 argumen, 2 argumen, maupun 3 argumen tanpa memicu TypeError: missing required positional arguments. 
    Jika sebuah data tidak dikirimkan, Python akan diam-diam menutupi lubang tersebut menggunakan nilai bawaan yang telah 
    ditetapkan di awal.

    Reduksi Redundansi Kode: Dalam kasus kalkulasi harga, kenyataannya 90% pelanggan tidak memiliki kupon diskon (diskon = 0) 
    dan semua pelanggan dikenakan besaran pajak yang sama (pajak = 5%). Daripada memaksa programmer menulis net_price(500, 0, 
    0.05) setiap kali ingin menghitung harga normal, menetapkan discount=0 dan tax=0.05 pada parameter akan sangat menghemat 
    waktu penulisan kode.

    Hukum Posisi Parameter (Non-Default Must Precede Default): Python memiliki satu aturan tata bahasa (syntax) yang ketat 
    mengenai teknik ini. Anda wajib meletakkan parameter yang wajib diisi (tidak punya nilai default) di urutan paling depan, 
    baru diikuti oleh parameter opsional (yang punya nilai default) di belakangnya. Jika Anda menulis def count(start=0, end):, 
    Python akan kebingungan saat Anda hanya mengirimkan satu angka seperti count(5). Ia tidak tahu apakah angka 5 itu ditujukan 
    untuk menimpa nilai start, atau untuk mengisi nilai end yang kosong.
"""