from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Database variable initialization
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']

        my_data = Product(name, price, quantity)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))