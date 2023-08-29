maara = 0

while True:
    kayttajatunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    maara += 1

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif maara >= 5:
        print("Olet ylittänyt 5 yritystä. Yritä myöhemmin uudelleen.")
        break
    else:
        print("Pääsy evätty")



