#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<param>')
def print_string(param):
    print(param)
    return f'{param}'

@app.route('/count/<param>')
def count(param):
    return ''.join([str(i) + '\n' for i in range(int(param))])

@app.route('/math/<num1>/<op>/<num2>')
def math(num1, op, num2):
    n1, n2 = int(num1), int(num2)
    dict = {
        '+': n1 + n2,
        '-': n1 - n2,
        '*': n1 * n2,
        'div': n1 / n2,
        '%': n1 % n2
    }
    return str(dict[op])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
