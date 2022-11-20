from flask import Flask

app = Flask(__name__)
@app.route('/Alku/<Number>')
def Alku(Number):
    parit = []
    arvo = 0
    while arvo < int(Number):
        arvo += 1
        if int(Number) % arvo == 0:
            parit.append(arvo)
    if len(parit) <=2:
        vastaus = {
            "Number": Number,
            "isPrime" : True
        }
    else:
        vastaus = {
            "Number" : Number,
            "isPrime" : False
        }

    return str(vastaus)

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port=3000)