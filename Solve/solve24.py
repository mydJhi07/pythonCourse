pemain1 = input("P1: ")
pemain2 = input("P2: ")

if (pemain1 == "gunting"):
    if (pemain2 == "gunting"):
        print("Seri")
    elif (pemain2 == "kertas"):
        print("Pemain 1 menang")
    elif (pemain2 == "batu"):
        print("Pemain 2 menang")

elif (pemain1 == "batu"):
    if (pemain2 == "gunting"):
        print("Pemain 1 menang")
    elif (pemain2 == "kertas"):
        print("Pemain 2 menang")
    elif (pemain2 == "batu"):
        print("Seri")

elif (pemain1 == "kertas"):
    if (pemain2 == "gunting"):
        print("Pemain 2 menang")
    elif (pemain2 == "kertas"):
        print("Seri")
    elif (pemain2 == "batu"):
        print("Pemain 1 menang")
