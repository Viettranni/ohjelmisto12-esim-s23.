import mysql.connector

def haeLentokenttienMaarat(ident):
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
        sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
        kursori.execute(sql, (ident,))

        # Hae tulokset
        tulokset = kursori.fetchall()

        if tulokset:
            print(f"Lentokenttien lukumäärä maassa {ident} tyypeittäin:")
            for tulos in tulokset:
                lentokentta_tyyppi, lukumaara = tulos
                if lentokentta_tyyppi == "small_airport":
                    kuvaus = "Pieniä lentokenttiä"
                elif lentokentta_tyyppi == "medium_airport":
                    kuvaus = "Keskikokoisia lentokenttiä"
                elif lentokentta_tyyppi == "heliport":
                    kuvaus = "Helikopterikenttiä"
                elif lentokentta_tyyppi == "closed":
                    kuvaus = "Suljetut kentät"
                elif lentokentta_tyyppi == "balloonport":
                    kuvaus = "Balloonports"
                elif lentokentta_tyyppi == "seaplane":
                    kuvaus = "Seaplaneja "

                print(f"{kuvaus} on: {lukumaara} kpl.")
        else:
            print(f"Maassa {ident} ei ole lentokenttiä.")
    except mysql.connector.Error as e:
        print("Virhe tietokantayhteydessä:", str(e))
    finally:
        # Suljetaan kursori ja tietokantayhteys
        kursori.close()
        yhteys.close()


ident = input("Anna maakoodi: ").upper()
haeLentokenttienMaarat(ident)
