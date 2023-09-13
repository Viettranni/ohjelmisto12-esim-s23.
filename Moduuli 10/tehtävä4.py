import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, speed):
        if speed >= 0:
            self.tamanhetkinen_nopeus = min(self.tamanhetkinen_nopeus + speed, self.huippunopeus)
        else:
            self.tamanhetkinen_nopeus = max(self.tamanhetkinen_nopeus + speed, 0)

    def kulje(self, tuntimaara):
        self.kuljettu_matka += (self.tamanhetkinen_nopeus * tuntimaara)

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot = autot
        self.voittaja = ''

    def lisaa_auto(self, auto):
        self.autot.append(auto)

    def tunti_kuluu(self):
        for auto in self.autot:
            speed_change = random.randint(-20, 20)
            auto.kiihdyta(speed_change)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailun nimi: {self.kilpailun_nimi}")
        print(f"Pituus: {self.pituus_km}")
        print("Autot")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                self.voittaja = auto.rekisteritunnus
                return True
            else:
                return False

def main():
    autot = list()

    i = 0
    while i < 10:
        uusi_auto = Auto(f"ABC-{i}", random.randint(100, 200))
        autot.append(uusi_auto)
        i += 1

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    while True:
        if kilpailu.kilpailu_ohi():
            kilpailu.tulosta_tilanne()
            print(f'Kilpailun voitti auto: \n {kilpailu.voittaja}')
            break
        else:
            random.shuffle(kilpailu.autot)
            kilpailu.tunti_kuluu()


if __name__ == "__main__":
    main()