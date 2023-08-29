while True:
    number = float(input("Muunnan tuumat centtimetreiksi. Syötä tuuma: "))
    cm = number * 2.54

    if number <= 0:
        print("Kiitos käynnistä!")
        break
    else:
        print(f"{number} tuumaa on centtimetreinä {cm}.")
