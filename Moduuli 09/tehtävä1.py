class Auto:
    tehty = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0


auto1 = Auto("ABC-123", 142)
print("Auton ominaisuudet:")
print(f"Rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus} km/h.")
print(f"Tämän hetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h.")
print(f"Kuljettu matka: {auto1.kuljettu_matka} km")
