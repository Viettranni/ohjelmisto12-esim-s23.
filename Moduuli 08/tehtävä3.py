import mysql.connector
from geopy.distance import geodesic

def Lentokenttä_etaisyys(ident):
    try:
        # Muodostetaan yhteys tietokantaan
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='1234',
            autocommit=True
        )

        # Luo kursori
        kursori = yhteys.cursor()

        # Suorita SQL-kysely
        sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        kursori.execute(sql, (ident,))

        # Hae tulokset
        tulos = kursori.fetchone()

        if tulos:
            lentokentta_nimi, latitude, longitude = tulos
            print(f"Lentokenttä: {lentokentta_nimi}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            return lentokentta_nimi, latitude, longitude
        else:
            print("Lentokenttää ei löytynyt ICAO-koodilla:", ident)
            return None, None, None
    except Exception as e:
        print("Virhe tietokantayhteydessä:", str(e))
        return None, None, None
    finally:
        # Suljetaan kursori ja tietokantayhteys
        kursori.close()
        yhteys.close()


ident1 = input("Anna ensimmäinen ICAO-koodi: ")
ident2 = input("Anna toka ICAO-koodi: ")

lentokentta_nimi1, latitude1, longitude1 = Lentokenttä_etaisyys(ident1)
lentokentta_nimi2, latitude2, longitude2 = Lentokenttä_etaisyys(ident2)

if latitude1 is not None and longitude1 is not None and latitude2 is not None and longitude2 is not None:
    point1 = (latitude1, longitude1)
    point2 = (latitude2, longitude2)
    etaisyys = geodesic(point1, point2).kilometers
    print(f"Etäisyys kohteen {lentokentta_nimi1} ja {lentokentta_nimi2} välillä on {etaisyys:.2f} kilometriä!")

