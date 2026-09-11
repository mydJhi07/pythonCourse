import random

# ==========================================
# 1. DEKLARASI STATE & STRUKTUR DATA
# ==========================================
# Menggunakan Tuple karena opsi tidak akan pernah berubah (Immutable)
options = ("rock", "paper", "scissors")
playing = True # Bendera (Flag) untuk mengontrol siklus program utama

# ==========================================
# 2. SIKLUS PROGRAM UTAMA (MAIN LOOP)
# ==========================================
while playing:
    # Reset variabel pada setiap iterasi baru
    player = None
    computer = random.choice(options)
    
    # ==========================================
    # 3. VALIDASI INPUT (WHILE TRAP)
    # ==========================================
    # Program akan mengurung user di dalam loop ini 
    # sampai input yang diberikan benar-benar ada di dalam tuple 'options'.
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        
    print(f"\nPlayer   : {player}")
    print(f"Computer : {computer}")
    
    # ==========================================
    # 4. EVALUASI KONDISI (BOOLEAN LOGIC)
    # ==========================================
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        # Jika bukan seri dan tidak memenuhi syarat menang, pasti kalah.
        print("You lose!")
        
    # ==========================================
    # 5. MEKANISME TERMINASI (EXIT STRATEGY)
    # ==========================================
    play_again = input("\nPlay again? (y/n): ").lower()
    
    # Jika input BUKAN 'y', ubah flag menjadi False untuk membunuh Main Loop
    if play_again != "y":
        playing = False

print("Thanks for playing!")