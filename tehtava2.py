from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/kentta/<ident>')
def kentta(ident):
    sql = f'''SELECT airport.name, municipality FROM airport 
    WHERE ident= "{ident}";'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            vastaus = {
                "ICAO" : ident,
                "name" : rivi[0],
                "municipality" : rivi[1]
            }
    return vastaus
    kentta(ident)


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='fl1ght_game',
         user='root',
         password='vaahtokarkki',
         autocommit=True
         )


if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port=3000)

