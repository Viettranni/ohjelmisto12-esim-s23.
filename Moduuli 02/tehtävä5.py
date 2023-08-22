while True:
    try:
        leiviskat = float(input("Anna leiviskät:"))
        naulat = float(input("Anna naulat:"))
        luodit = float(input("Anna luodit:"))
        break
    except ValueError:
        print("Yritä uudelleen. ")

# Muunnoskertoimet
LEIVISKA_TO_NAULA = 20
NAULA_TO_LUOTI = 32
LUOTI_TO_GRAM = 13.3
GRAM_TO_KG = 0.001

# Lasketaan KG ja G erikseen
KG = (leiviskat * LEIVISKA_TO_NAULA * NAULA_TO_LUOTI * LUOTI_TO_GRAM * GRAM_TO_KG) + (
            naulat * NAULA_TO_LUOTI * LUOTI_TO_GRAM * GRAM_TO_KG) + (luodit * LUOTI_TO_GRAM * GRAM_TO_KG)

G = (KG - int(KG)) * 1000

print(f"Massa nykymittojen mukaan:")
print(f"{int(KG)} kilogrammaa ja {G:.2f} grammaa.")
