from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
            return conn
        except:
            time.sleep(2)

@app.route('/')
def home():
    conn = connect_db()
    return "Flask + MySQL CI/CD is Working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
