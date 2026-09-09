import time

waktuku = int(input())

while waktuku >= 1:

    detik = waktuku % 60
    menit = int(waktuku / 60) % 60
    jam = int(waktuku / 3600)

    print(f"{jam:02}:{menit:02}:{detik:02}")
    time.sleep(1)

    waktuku = waktuku - 1
