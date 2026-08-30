import math

a, b, c = map(float, input().split())
temp = 0

if (max(a, b, c) != c):
    if (a > b):
        temp = c
        c = max(a, b, c)
        a = temp
    elif (b > a):
        temp = c
        c = max(a, b, c)
        b = temp
    else:
        temp = c
        c = max(a, b, c)
        a = temp

"""
bisa juga menggunakan ini untuk menentukan apakah c terbesar
if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

"""

if (a > 0 and b > 0 and c > 0):

    if (a + b > c and a + c > b and b + c > a):

        if (a == b and b == c):
            print("Segitiga sama sisi")
        elif (a == b or b == c or a == c):
            print("Segitiga sama kaki")
        else:
            if (pow(a, 2) + pow(b, 2) == pow(c, 2)):
                print("Segitiga sembarang, Siku-siku")
            elif (pow(a, 2) + pow(b, 2) > pow(c, 2)):
                print("Segitiga sembarang, lancip")
            elif (pow(a, 2) + pow(b, 2) < pow(c, 2)):
                print("Segitiga sembarang, tumpul")
    else:
        print("Bukan segitiga")

else:
    print("Nilai harus bernilai positif")
