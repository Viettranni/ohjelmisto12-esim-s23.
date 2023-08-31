import math
def pizzan_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade**2)
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta


def main():
    pizza1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija(cm): "))
    pizza1_hinta = float(input("Anna ensimmäisen pizzan hinta: "))
    pizza2_halkaisija = float(input("Anna toisen pizzan halkaisija(cm): "))
    pizza2_hinta = float(input("Anna toisen pizzan hinta: "))

    yksikkohinta1 = pizzan_yksikkohinta(pizza1_halkaisija, pizza1_hinta)
    yksikkohinta2 = pizzan_yksikkohinta(pizza2_halkaisija, pizza2_hinta)

    if yksikkohinta1 < yksikkohinta2:
        parempi_pizza = "Ensimmäinen pizza"
    else:
        parempi_pizza = "Toinen pizza"

    print(f"\n{parempi_pizza} antaa paremman vastineen rahalle.")

main()