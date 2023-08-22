leiviskat = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

# Muunnoskertoimet
LEIVISKA_TO_NAULA = 20
NAULA_TO_LUOTI = 32
LUOTI_TO_GRAM = 13.3
GRAM_TO_KG = 0.001

# Laskelmat
grammat = (leiviskat * LEIVISKA_TO_NAULA * NAULA_TO_LUOTI * LUOTI_TO_GRAM) + (
            naulat * NAULA_TO_LUOTI * LUOTI_TO_GRAM) + (luodit * LUOTI_TO_GRAM)
kilogrammat = grammat * GRAM_TO_KG

print(f"Massa nykymittojen mukaan:")
print(f"{int(kilogrammat)} kilogrammaa ja {grammat:.2f} grammaa.")