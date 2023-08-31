lentoasemat = {'EFHK' : 'Helsinki',}

while True:
    print("1 = Uuden lentoaseman syöttäminen -- 2 = Lentokentän haku -- 3 = Lopettaa ohjelma ")
    paatos = input("Valitse 1-3 mitä haluat tehdä? ")

    if paatos == "1":
        print("Tarvitsen sinulta lentoaseman ICAO-koodin ja nimen. ")
        ICAO = input("ICAO-koodi: ")
        lentokentan_nimi = input("Lentokentän nimi: ")
        lentoasemat[ICAO] = lentokentan_nimi
        print("Kiitos! Tiedot tallennettu järjestelmäämme.")

    elif paatos == "2":
        ICAO = input("Syötä lentokentän CIAO-koodi: ")
        if ICAO in lentoasemat:
            print(f"{ICAO}-koodin lentokenttä on {lentoasemat[ICAO]}!")
        else:
            print("Lentoasemaa ei löydy, voit lisätä sen 1. valinnassa. Yritä uudelleen.")

    elif paatos == "3":
        print("Mukavaa päivän jatkoa!")
        break

    else:
        ("Virheellinen valinta. Valitse 1, 2 tai 3!")
