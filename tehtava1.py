from flask import Flask, request

app = Flask(__name__)
@app.route('/alku')
def alku():
    args = request.args
    Number = float(args.get("Number"))
    parit = []
    arvo = 0
    while arvo < Number:
        arvo += 1
        if Number % arvo == 0:
            parit.append(arvo)
    if len(parit) <=2:
        vastaus = {
            "Number": (f'{Number:.0f}'),
            "isPrime" : True
        }
    else:
        vastaus = {
            "Number" : (f'{Number:.0f}'),
            "isPrime" : False
        }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port=3000)



#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku
#alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
#Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
