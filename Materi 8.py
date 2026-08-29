# Calculator

print("===== KALKULATOR =====\n")

operator = input("Masukkan operator (+ - * /): ")
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = num1 + num2
    print(hasil)
elif operator == "-":
    hasil = num1 - num2
    print(hasil)
elif operator == "*":
    hasil = num1 * num2
    print(hasil)
elif operator == "/":
    hasil = num1 / num2
    print(hasil)
else:
    print(f"{operator} tidak valid\n")

print("===== KONVERSI BERAT =====\n")

berat = float(input("Masukkan berat anda: "))
unit = input("satuan kilogram atau satuan pound? (K atau L) ")

if unit == "K":
    berat *= 2.025
    unit = "Lbs"
    print(f"Beratmu adalah {round(berat, 2)} {unit}")
elif unit == "L":
    berat /= 2.025
    unit = "kg"
    print(f"Beratmu adalah {round(berat, 2)} {unit}")
else:
    print(f"{unit} tidak valid")

