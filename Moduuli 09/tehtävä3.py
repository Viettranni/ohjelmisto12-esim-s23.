class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        if nopeuden_muutos >= 0:
            # Kiihdytä, mutta älä ylitä huippunopeutta
            self.tamanhetkinen_nopeus = min(self.tamanhetkinen_nopeus + nopeuden_muutos, self.huippunopeus)
        else:
            # Hidasta, mutta älä mene negatiiviseksi
            self.tamanhetkinen_nopeus = max(self.tamanhetkinen_nopeus + nopeuden_muutos, 0)

    def kulje(self, tuntimaara):
        # Laske etäisyys matkustetun ajan ja nykyisen nopeuden perusteella
        matka = self.tamanhetkinen_nopeus * tuntimaara
        # Lisää matka kuljetun matkan kokonaismäärään
        self.kuljettu_matka += matka

    def tulosta_nopeus(self):
        print(f"Auton nopeus on {self.tamanhetkinen_nopeus} km/h.")

    def tulosta_matka(self):
        print(f"Kuljettu matka on {self.kuljettu_matka} km.")

# Pääohjelma

    # Luo uusi auto-olio
auto1 = Auto("ABC-123", 142)

auto1.tulosta_nopeus()
auto1.tulosta_matka()

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

auto1.tulosta_nopeus()

auto1.kulje(1.5)

auto1.tulosta_matka()
