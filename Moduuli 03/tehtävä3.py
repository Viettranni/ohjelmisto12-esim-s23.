while True:
    sukupuoli = input("Mikä on biologinen sukupuolesi? ").lower()

    if sukupuoli not in ["mies", "nainen"]:
        print("Virheellinen syöte. Syötä mies tai nainen.")
        continue

    while True:
        try:
            hemoglobiiniarvo = float(input("Anna hemoglobiini arvosi. "))
            break
        except ValueError:
            print("Virheellinen syöte. Syötä numeerinen arvo.")

    if sukupuoli == "mies":
        if 134 < hemoglobiiniarvo < 195:
            print("Sinulla on normaali hemoglobiiniarvo.")
            break
        elif 195 <= hemoglobiiniarvo:
            print("Sinulla on korkea hemoglobiiniarvo. ")
            break
        elif 134 >= hemoglobiiniarvo:
            print("Sinulla on matala hemoglobiiniarvo. ")
            break

    elif sukupuoli == "nainen":
        if 117 < hemoglobiiniarvo < 175:
            print("Sinulla on normaali hemoglobiiniarvo.")
            break
        elif 175 <= hemoglobiiniarvo:
            print("Sinulla on korkea hemoglobiiniarvo. ")
            break
        elif 117 >= hemoglobiiniarvo:
            print("Sinulla on matala hemoglobiiniarvo. ")
            break

    else:
        print("Syötä mies/nainen.")