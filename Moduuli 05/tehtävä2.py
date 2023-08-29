lista = []

while True:
    lukuja = input("Anna lukuja! (Vähintään 5 lukua!) ")

    if lukuja == "":
        break

    luku = int(lukuja)
    lista.append(luku)


lista.sort(reverse=True)
viisi = [lista[0], lista[1], lista[2], lista[3], lista[4]]
print(f"Viisi suurinta lukua: {viisi}")
