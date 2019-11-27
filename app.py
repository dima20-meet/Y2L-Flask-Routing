from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route('/store')
def hello_store():
	return render_template("store.html", products = query_all())

@app.route('/cart')
def hello_cart():
	return render_template("cart.html")
	

@app.route('/about')
def hello_about():
	return render_template("about.html")	

@app.route('/add_to_cart/<int:productID>')
def addToCart(productID):
	#Take productID, and create a new cart item.
	return render_template("store.html")
##### Code here ######



#####################


if __name__ == '__main__':
    app.run(debug=True)