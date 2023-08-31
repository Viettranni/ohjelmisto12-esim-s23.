import random

def main():
    silmäluku = int(input("Syötä nopan suurin silmäluku: "))
    tahkot = silmäluku

    while True:
        kierros = random.randint(1, tahkot)
        print("Heitto:", kierros)

        if kierros == silmäluku:
            print("Silmäluku löytyi!!")
            break
main()