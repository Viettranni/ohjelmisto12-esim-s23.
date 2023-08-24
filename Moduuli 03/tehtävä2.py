while True:
    hyttiluokka = input("Mikä on laivan hyttiluokka? (LUX, A, B, C) \n").upper()

    if hyttiluokka == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
        break
    elif hyttiluokka == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
        break
    elif hyttiluokka == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
        break
    elif hyttiluokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
        break
    else:
        print("Virheellinen hyttiluokka.")
