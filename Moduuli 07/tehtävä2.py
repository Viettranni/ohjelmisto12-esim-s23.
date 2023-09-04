lista = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        print(lista)
        break
    elif nimi in lista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        lista.add(nimi)

for nimi in lista:
   print(nimi)
