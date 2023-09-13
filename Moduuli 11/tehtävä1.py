class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}: ")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self. kirjoittaja = kirjoittaja
        self.sivumaara = int(sivumaara)
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija: {self.kirjoittaja}, {self.sivumaara} sivua.")


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", "200"))

for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()