import math

p, r, t = map(float, input().split())

a = p * pow(1 + (r / 100), t)

print(f"Saldo akhir = {round(a, 2)}")
