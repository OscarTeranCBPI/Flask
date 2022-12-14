from flask import Flask
from flask import render_template, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is {}</p>'.format(user_agent)

# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

# @app.route('/')
# def index():
#     return redirect('http://www.example.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


# Dynamic Routes
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

