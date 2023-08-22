import random

def kolmenkoodi():
    code = ""
    for _ in range(3):
        numeroa = str(random.randint(0, 9))
        code += numeroa
    return code

def neljankoodi():
    code = ""
    for _ in range(4):
        numeroa = str(random.randint(1, 6))
        code += numeroa
    return code

def main():
    kolme = kolmenkoodi()
    nelja = neljankoodi()

    print("Kolmenumeroisen koodin arvonta:", kolme)
    print("Nelinumeroisen koodin arvonta:", nelja)

main()


