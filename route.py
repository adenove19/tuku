from app import app
from models.db import coba
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/addproduct")
def addproduct():
    return render_template('add-new-product.html')

@app.route("/order")
def order():
    return render_template('order.html')

@app.route("/profil")
def profil():
    return render_template('profil-toko.html')