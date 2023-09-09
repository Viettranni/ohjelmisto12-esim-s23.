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

    def tulosta_nopeus(self):
        print(f"Auton nopeus on {self.tamanhetkinen_nopeus} km/h.")

    def tulosta_ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka:.2f} km")
        print(f"Tämän hetkinen nopeus: {self.tamanhetkinen_nopeus} km/h\n")

def cars():
    car_list = []
    for i in range(10):
        registration_number = f"ABC-{i+1}"
        huippunopeus = random.randint(100, 201)
        car_list.append(Auto(registration_number, huippunopeus))
    return car_list

def kilpailu():
    car_list = cars()

    while True:
        for auto in car_list:
            speed = random.randint(-10, 15)
            auto.kiihdyta(speed)
            # Seuraavassa parametrissä oleva 1 edustaa yhtä tuntia, koska autojen matkaa päivystetään tunnin välein.
            auto.kulje(1)

        voittaja = None
        for auto in car_list:
            if auto.kuljettu_matka >= 10000:
                voittaja = auto
                break

        if voittaja:
            print("Kilpailun voitti seuraava auto: ")
            voittaja.tulosta_ominaisuudet()
            break

kilpailu()

