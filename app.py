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
    my_data = Product.query.all()
    return render_template("index.html", products = my_data)

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

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Product.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.price = request.form['price']
        my_data.quantity = request.form['quantity']

        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Product.query.get(id)
    db.session.delete(my_data)

    db.session.commit()
    return redirect(url_for('index'))