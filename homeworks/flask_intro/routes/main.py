from flask import Flask
from app import app


@app.route('/')
def home():
    return 'go to /add/%num1/%num2 to get the result of addition'

@app.route('/add/<num1>/<num2>')
def add_operation(num1, num2):
    res = int(num1) + int(num2)
    return str(res)
