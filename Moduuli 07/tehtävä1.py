while True:
    kuukausi = int(input("Anna kuukauden numero (esim. tammikuu syötä 1!) "))
    vuoden_aika = ("talvi", "kevät", "kesä", "syksy")

    if kuukausi > 12 or kuukausi < 1:
        print("Vaihtoehtoja on vain 1-12. Syötä uudelleen.")
    elif kuukausi in range(3, 6):
        vuodenaika = vuoden_aika[1]
        break
    elif kuukausi in range(6, 9):
        vuodenaika = vuoden_aika[2]
        break
    elif kuukausi in range(9, 12):
        vuodenaika = vuoden_aika[3]
        break
    else:
        vuodenaika = vuoden_aika[0]
        break

print(f"Vuoden aika on {vuodenaika}!")