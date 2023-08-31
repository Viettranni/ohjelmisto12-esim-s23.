def parittomien_lukujen_poisto(numerot):
    parilliset = [num for num in numerot if num % 2 == 0]
    return parilliset

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset = parittomien_lukujen_poisto(lista)
    print("Alkuperäinen lista:", lista)
    print("Karsittu lista:", parilliset)

main()
