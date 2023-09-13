import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, speed):
        if speed >= 0:
            self.tamanhetkinen_nopeus = min(self.tamanhetkinen_nopeus + speed, self.huippunopeus)
        else:
            self.tamanhetkinen_nopeus = max(self.tamanhetkinen_nopeus + speed, 0)

    def kulje(self, tuntimaara):
        self.kuljettu_matka += (self.tamanhetkinen_nopeus * tuntimaara)

    def __str__(self):
        return f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km"


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
    def __str__(self):
        return super().__str__() + f", Akkukapasiteetti: {self.akkukapasiteetti} kWh"

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

    def __str__(self):
        return super().__str__() + f", Bensatankki: {self.bensatankki} litraa"


def main():
    autot = []

    autot.append(Sähköauto("ABC-15", "180", "52.5"))
    autot.append(Polttomoottoriauto("ACD-123", "165", "32.3"))

    # Asetetaan nopeudet ja ajettaan
    for auto in autot:
        auto.kiihdyta(random.randint(5, 40))
        auto.kulje(3)

    # Tulostetaan autojen tiedot
    for auto in autot:
        print(auto)


if __name__ == "__main__":
    main()
