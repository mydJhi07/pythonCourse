rahasia = 7
cobaan = 0

while rahasia != 7:
    cobaan = cobaan + 1

    tebakan = int(input("Tebak: "))

    if (tebakan < 7):
        print("Terlalu rendah, coba lagi")
    elif (tebakan > 7):
        print("Terlalu tinggi, coba lagi")
