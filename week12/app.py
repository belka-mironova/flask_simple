from flask import Flask, render_template
import database


app = Flask(__name__)

@app.route("/")
def hello_world():
    suppliers = database.get_all_facts()
    return render_template('index.html', suppliers = suppliers)


@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    names = database.get_supplier_name(supplier_id)
    return render_template('products.html', products = products, names = names)


@app.route("/categories")
def categories():
    categories = database.get_cat_info()
    return render_template('categories.html', categories = categories)


@app.route("/categories/<int:category_id>")
def cat_products(category_id):
    products = database.get_category_products(category_id)
    return render_template('cat_products.html', products = products)