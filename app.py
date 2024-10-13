from flask import Flask, render_template
from connect import db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM krindustriesdb.products")  
    products = cursor.fetchall()
    return render_template('products.html', products=products)


@app.route('/customers_orders')
def customers_orders():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT customers.CustomerID, customers.CompanyName, customers.ContactName, 
               orders.OrderID, orders.OrderDate, orders.TotalAmount, orders.Status
        FROM krindustriesdb.customers
        LEFT JOIN krindustriesdb.orders 
        ON customers.CustomerID = orders.CustomerID;
    """)
    customers_orders = cursor.fetchall()

    return render_template('customers_orders.html', customers_orders=customers_orders)



@app.route('/inventory')
def inventory():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM krindustriesdb.inventory") 
    inventory = cursor.fetchall()
    return render_template('inventory.html', inventory=inventory)


@app.route('/productiontasks')
def productiontasks():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM krindustriesdb.productiontasks")  
    productiontasks = cursor.fetchall()
    return render_template('productiontasks.html', productiontasks=productiontasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
