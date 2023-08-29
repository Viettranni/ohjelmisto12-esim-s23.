import random
lista = []

while True:
    luku = input("Syötä arpakuutioiden lukumäärä! ")

    if luku == "":
        print("Kiitos ajastasi!")
        break
    luku = int(luku)
    summa = 0

    for i in range(luku):
        arpakuutio = random.randint(1, 6)
        lista.append(arpakuutio)
        summa += arpakuutio
    print(summa)


