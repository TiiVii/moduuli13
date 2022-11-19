from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vaahtokarkki'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/kenttä')


cursor = mysql.connection.cursor()

cursor.execute('''''')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)