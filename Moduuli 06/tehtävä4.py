def kokonaislukujen_summa(numeroja):
    yhteensa = sum(numeroja)
    return yhteensa

def main():
    lista = [2,4,1,5,6]
    tulos = kokonaislukujen_summa(lista)
    print("Listan lukujen summa on:", tulos)

main()