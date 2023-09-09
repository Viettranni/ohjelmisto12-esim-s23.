class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, kmh):
        if kmh > self.huippunopeus or kmh < 0:
            self.tamanhetkinen_nopeus = min(self.tamanhetkinen_nopeus + kmh, self.huippunopeus)
        else:
            self.tamanhetkinen_nopeus = max(self.tamanhetkinen_nopeus + kmh, 0)

    def tulosta_nopeus(self):
        print(f"Auton nopeus on {self.tamanhetkinen_nopeus} km/h. ")



auto1 = Auto("ABC-123", 142)
print("Auton ominaisuudet:")
print(f"Rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus} km/h.")
print(f"Tämän hetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h.")
print(f"Kuljettu matka: {auto1.kuljettu_matka} km")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

auto1.kiihdyta(-200)

auto1.tulosta_nopeus()