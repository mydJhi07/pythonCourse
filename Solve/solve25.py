x, y = map(float, input().split())

if (x > 0 and y > 0):
    print("Kuadran I")
elif (x < 0 and y > 0):
    print("Kuadran II")
elif (x < 0 and y < 0):
    print("Kuadran III")
elif (x > 0 and y < 0):
    print("Kuadran IV")
elif (x == 0 and y != 0):
    print("Sumbu-Y")
elif (y == 0 and x != 0):
    print("Sumbu-X")
else:
    print("Titik Asal")
