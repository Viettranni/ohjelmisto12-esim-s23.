import random

arvonta_luku = random.randint(1, 10)

while True:
    arvonta = int(input("Arvaa oikea numero!"))

    if arvonta < arvonta_luku:
        print("Liian pieni arvaus. Yritä uudelleen!")
    elif arvonta > arvonta_luku:
        print("Liian suuri arvaus. Yritä uudelleen!")
    elif arvonta == arvonta_luku:
        print("Oikein!")
        break
