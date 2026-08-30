import math

PI = round(22 / 7, 2)  # dibulatkan dua angka di belakang koma

jariJari = float(input())

luas = PI * (jariJari ** 2)

keliling = 2 * PI * jariJari

print(f"Luas: {round(luas, 2)}")
print(f"Keliling: {round(keliling, 2)}")
