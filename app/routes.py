from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




@app.route('/hello')
def hello_again():
    return "Hello, world!"

@app.route('/info')
def info():
    return f'This is an information page.'

@app.route('/calc/<int:a>/<int:b>')
def calc(a,b):
    summ = a + b
    return f'The sum of {a} and {b} is {summ}'

@app.route('/reverse/<string>')
def reverse(string):
    return string[::-1]

@app.route('/user/<name>/<int:age>')
def user(name,age):
    return f'Hello, {name}. You are {age} years old.'