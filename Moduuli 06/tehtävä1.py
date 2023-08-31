import random
def main():
    while True:
        arpoa = random.randint(1, 6)

        if arpoa == 6:
            print("6")
            print("Löysimme oikean numeron!")
            break
        else:
            print(arpoa)
main()