import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def airport(ident):
    try:
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='1234',
            autocommit=True
        )

        kursori = yhteys.cursor()

        sql = "SELECT name, municipality FROM airport WHERE ident = %s"
        kursori.execute(sql, (ident,))

        tulos = kursori.fetchone()

        if tulos:
            name, municipality = tulos
            return name, municipality
        else:
            print("Lentokenttää ei löytynyt ICAO-koodilla:", ident)
            return None, None

    except Exception as e:
        print("Virhe tietokantayhteydessä:", str(e))
        return None, None
    finally:
        # Suljetaan kursori ja tietokantayhteys
        kursori.close()
        yhteys.close()

@app.route('/ident/<string:ident>')
def airports(ident):
    name, municipality = airport(ident)
    response = {"ICAO": ident, "Name": name, "Municipality": municipality}
    return jsonify(response)

if __name__ == '__main__':
    app.run()