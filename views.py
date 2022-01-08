# from flask import render_template, request, redirect, url_for
# from app import app, Product
# from . import db

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/add', methods = ['POST'])
# def add():
#     if request.method == 'POST':
#         name = request.form['name']
#         price = request.form['price']
#         quantity = request.form['quantity']

#         my_data = Product(name, price, quantity)
#         db.session.add(my_data)
#         db.session.commit()

#         return redirect(url_for('index'))