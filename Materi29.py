import random

# ==========================================
# 1. DEKLARASI DICTIONARY ASCII ART
# ==========================================
# Menyimpan desain dadu. Key = Angka Dadu (1-6). 
# Value = Tuple yang berisi 5 baris string pembentuk dadu.
dice_art = {
    1: ("┌───────┐", 
        "│       │", 
        "│   ●   │", 
        "│       │", 
        "└───────┘"),
    2: ("┌───────┐", 
        "│ ●     │", 
        "│       │", 
        "│     ● │", 
        "└───────┘"),
    3: ("┌───────┐", 
        "│ ●     │", 
        "│   ●   │", 
        "│     ● │", 
        "└───────┘"),
    4: ("┌───────┐", 
        "│ ●   ● │", 
        "│       │", 
        "│ ●   ● │", 
        "└───────┘"),
    5: ("┌───────┐", 
        "│ ●   ● │", 
        "│   ●   │", 
        "│ ●   ● │", 
        "└───────┘"),
    6: ("┌───────┐", 
        "│ ●   ● │", 
        "│ ●   ● │", 
        "│ ●   ● │", 
        "└───────┘")
}

dice = []
total = 0

# ==========================================
# 2. AKUISISI & GENERASI DATA
# ==========================================
num_of_dice = int(input("How many dice?: "))

# Mengisi list 'dice' dengan angka acak 1-6 sebanyak jumlah dadu yang diminta
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Kalkulasi total nilai dadu
for die in dice:
    total += die

# ==========================================
# 3. ALGORITMA RENDERING HORIZONTAL (NESTED LOOP)
# ==========================================
# Outer loop: Berjalan 5 kali (karena tinggi 1 dadu adalah 5 baris)
for line in range(5):
    # Inner loop: Menelusuri setiap hasil lemparan dadu yang ada di list
    for die in dice:
        # Mengambil Tuple dadu dari dictionary, lalu mencetak baris ke-'line'
        # end="" mencegah pindah baris, sehingga irisan dadu dicetak menyamping
        print(dice_art.get(die)[line], end="")
        
    # Pindah baris hanya setelah 1 irisan horizontal dari SEMUA dadu selesai dicetak
    print()

print(f"Total: {total}")