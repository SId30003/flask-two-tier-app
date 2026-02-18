from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL CI/CD is Working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
