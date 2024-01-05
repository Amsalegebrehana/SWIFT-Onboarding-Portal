from flask import render_template, redirect, url_for
from app import app  
from model import User

@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route('/customers')
def list_customers():
    customers = User.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/customers/<int:customer_id>')
def view_customer(customer_id):
    customer = User.query.get(customer_id)
    return render_template('customer_details.html', customer=customer)

# @app.route('/customers/new', methods=['GET', 'POST'])
# def login():
#     # ... form handling and validation
#     new_customer = User(name=form.name.data, email=form.email.data)
#     app.db.session.add(new_customer)
#     app.db.session.commit()
#     return redirect(url_for('list_customers'))