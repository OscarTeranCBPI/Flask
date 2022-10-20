from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'


# Dynamic Routes
@app.route('/user/Oscar')
def user(Oscar):
    return '<h1>Hello, {}</h1>'.format(Oscar)

