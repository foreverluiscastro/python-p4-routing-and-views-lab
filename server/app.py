#!/usr/bin/env python3


from flask import Flask

app = Flask(__name__)

import ipdb

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ''
    for num in range(0, parameter):
        output += str(num) + '\n'

    return output

@app.route('/math/<string:num1>/<string:operation>/<string:num2>')
def math(num1, operation, num2):
    # ipdb.set_trace()
    if operation == "div":
        operation = "/"
    return str(eval(num1 + operation + num2))