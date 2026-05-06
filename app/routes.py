from app import app

@app.route('/')
def hello():
    return "Hello Flask!"

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