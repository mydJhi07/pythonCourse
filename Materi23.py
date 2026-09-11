# Program Quiz Game (Pilihan Ganda)

# 1. Deklarasi Data Quiz
# Pertanyaan disimpan dalam Tuple karena isinya tetap dan tidak boleh dimodifikasi saat runtime.
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

# Opsi jawaban disimpan dalam 2D Tuple.
# Tiap baris merepresentasikan empat pilihan ganda (A, B, C, D) untuk satu pertanyaan spesifik.
options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

# Kunci jawaban disimpan dalam Tuple.
answers = ("C", "D", "A", "A", "B")

# Wadah untuk menyimpan tebakan user (List) dan sistem skor.
guesses = []
score = 0
question_num = 0

# 2. Iterasi Menampilkan Pertanyaan (Outer Loop)
# Loop ini akan membedah setiap elemen dalam Tuple `questions`.
for question in questions:
    print("-------------------------")
    print(question)
    
    # 3. Menampilkan Opsi Jawaban (Menggunakan 2D Tuple)
    # Mengambil satu baris spesifik dari 'options' berdasarkan indeks 'question_num'.
    for option in options[question_num]:
        print(option)

    # 4. Input dan Validasi Jawaban
    # Meminta input pengguna dan mengonversinya menjadi huruf kapital (.upper()) 
    # agar sesuai dengan kunci jawaban, terlepas apakah mereka mengetik 'a' atau 'A'.
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    # Mengevaluasi jawaban
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
        
    # Berpindah ke indeks pertanyaan selanjutnya
    question_num += 1

# 5. Eksekusi Hasil Akhir (Results)
print("-------------------------")
print("       RESULTS           ")
print("-------------------------")

# Mencetak array kunci jawaban asli berdampingan
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print() # Pindah baris

# Mencetak array jawaban pengguna berdampingan
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# 6. Kalkulasi Persentase Skor
# Membagi total jawaban benar (score) dengan jumlah pertanyaan (len(questions)), dikali 100
score_percentage = int(score / len(questions) * 100)
print(f"Your score is: {score_percentage}%")

"""
    Penyusunan Data dengan Tuples: Program ini memanfaatkan keamanan data yang ditawarkan oleh Tuple. Variabel questions, 
    options (sebagai 2D Tuple), dan answers sengaja dibungkus sebagai Tuple dan bukan List karena konten dari struktur data ini
    murni bersifat konstan dan statis; tidak ada skenario di mana pengguna atau aplikasi berhak mengubah butir soal maupun kunci
    jawaban saat game berlangsung. Di sisi lain, riwayat tebakan (guesses) menggunakan List kosong ([]) agar bisa 
    memanjang (append) secara berurutan menyesuaikan respons pengguna.

    Pemetaan Sinkron (Synchronized Indexing): Mesin utama dari program ini berjalan di atas logika pemetaan indeks. Terdapat
    satu variabel sentral bernama question_num (dimulai dari 0). Ketika outer loop mengambil teks pertanyaan 0 dari array 
    questions, kode di bawahnya akan merujuk pada question_num untuk menarik baris opsi jawaban di indeks ke-0 dari 2D tuple
    options, lalu melakukan validasi evaluasi jawaban merujuk ke elemen indeks ke-0 di tuple answers. Sinkronisasi ini 
    memastikan soal, pilihan, dan kunci jawaban selalu relevan satu sama lain pada setiap pergantian putaran.

    Mekanisme Normalisasi Kasus (upper()): Sifat case-sensitivity Python bisa menyebabkan kesalahan evaluasi sepele. Jika 
    user mengetik 'c' sedangkan kuncinya adalah 'C', program akan menilainya salah jika diukur secara mentah. Fungsi .upper()
    menormalisasi seluruh input; entah user menekan capslock atau tidak, input akan dipaksa menjadi huruf kapital sebelum
    dilempar ke fase logika pencocokan (if guess == answers), sehingga meminimalisir kesalahan validasi fiktif.

    Sistem Evaluasi Matematis: Penghitungan skor tidak dilakukan dengan memberikan pembobotan absolut, melainkan perhitungan
    persentase secara matematis (score / jumlah pertanyaan * 100). Fungsi utilitas len(questions) membebaskan programer 
    dari pembatasan angka kaku (hardcoding); hal ini berarti programmer dapat menyisipkan lebih banyak butir soal baru ke
    dalam Tuple questions di kemudian hari, dan algoritma skoring persentase ini akan otomatis beradaptasi tanpa perlu menulis 
    ulang rumusnya.
"""