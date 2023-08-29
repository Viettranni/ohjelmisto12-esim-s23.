lista = []

while True:
    try:
        luku = input("Anna luku: ")
        if luku == "":
            print("EXIT")
            break
        luku = float(luku)
        lista.append(luku)
        lista.sort()
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku tai jätä tyhjäksi ja paina enter.")


if lista:
    print(f"Listan pienin luku on {lista[0]} ja listan suurin luku on {lista[-1]}.")
else:
    print("Et syöttänyt yhtään lukua")
