#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter  # Return plain text

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    # Join each number with \n and add an extra \n at the end for the test
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return Response(numbers, mimetype='text/plain')  # Return plain text with newline-separated numbers

# Math route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero)"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Please use one of +, -, *, div, %."

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
