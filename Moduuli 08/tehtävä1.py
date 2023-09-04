import mysql.connector

def haeLentokenttaTiedot(ident):
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
        sql = "SELECT name, municipality FROM airport WHERE ident = %s"
        kursori.execute(sql, (ident,))

        # Hae tulokset
        tulos = kursori.fetchone()

        if tulos:
            lentokentta_nimi, sijaintikunta = tulos
            print(f"Lentokenttä: {lentokentta_nimi}")
            print(f"Sijaintikunta: {sijaintikunta}")
        else:
            print("Lentokenttää ei löytynyt ICAO-koodilla:", ident)
    except Exception as e:
        print("Virhe tietokantayhteydessä:", str(e))
    finally:
        # Suljetaan kursori ja tietokantayhteys
        kursori.close()
        yhteys.close()


ident = input("Anna ICAO-koodi: ")
haeLentokenttaTiedot(ident)

