import random
def laske_pi(yhteis_pisteet):
    pisteet_inside_circle = 0

    for _ in range(yhteis_pisteet):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            pisteet_inside_circle += 1

    estimated_pi = 4 * pisteet_inside_circle / yhteis_pisteet
    return estimated_pi

def main():
    try:
        yhteis_pisteet = int(input("Syötä arvottavien pisteiden määrä: "))
        if yhteis_pisteet <= 0:
            print("Pisteiden määrän tulee olla positiivinen luku.")
            return
    except ValueError:
        print("Virheellinen syöte. Anna positiivinen kokonaisluku.")
        return

    estimated_pi = laske_pi(yhteis_pisteet)
    print(f"Laskettu likiarvo pi:lle {estimated_pi:.8f}")

main()
