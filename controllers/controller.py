from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/customer')
def index0():
    return render_template('order.html', title='Single Order', orders=orders)
