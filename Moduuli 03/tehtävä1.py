while True:
    pituus = float(input("Kuinka pitkä kuha on (cm)?"))
    if pituus <= 37:
        ero = 37 - pituus
        print(f"Sallitusta pyyntimitasta puuttuu {ero} cm. Laita kuha takaisin veteen.")
    elif pituus > 37:
        print(f"Onnittelut! Sait kalastettua {pituus}cm pituisen kuhan!")
        break
    else:
        print("Syötä centtimetreissä")