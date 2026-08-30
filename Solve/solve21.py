n, tempat = input().split()

n = int(n)

total = 0.0

if (tempat == "luar" and n > 0):
    if (n > 1):
        total = 15000 + 2000 * (n - 1)
        print(f"Ongkir = {total}")
    else:
        total = 15000
        print(f"Ongkir = {total}")
elif (tempat == "dalam" and n > 0):
    total = 10000
    print(f"Ongkir = {total}")
else:
    print("Input tidak valid")
