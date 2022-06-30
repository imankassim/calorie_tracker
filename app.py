import os
from flask import Flask, request, redirect, url_for
app = Flask(__name__)


@app.route('/')

@app.route('/home/<int:number>')
def home(number):
    output = number * number
    return str(output)

@app.route('/about')
def about():
    return "ABOUT PAGE"


@app.route('/redirect')
def redirect1():
    return "YOU HAVE BEEN REDIRECTED FROM HOME"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



#@app.route('/home', methods = ['GET', 'POST'])
#def home():
#    if request.method == 'POST':
#        return "POST method"
#    else:
#        return "GET method"



#@app.route('/home')
#def home():
#    return redirect(url_for('redirect1'))
#
#
#@app.route('/redirect')
#def redirect1():
#    return "YOU HAVE BEEN REDIRECTED FROM HOME"
