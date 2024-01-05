from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure MariaDB database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Amsa1e-Ge@localhost:3306/swiftconnectdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/requests')
def requests():
    return render_template("requests.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/signin", methods=['GET', 'POST'])
def signIn():
    print('here')
    email = request.form['email']
    password = request.form['password']

    print(email, password)

    if email and password:
        # return json.dumps({'validation' : validateUser(email, password)})
        return render_template("index.html") 
    return  json.dumps({'validation' : False})

def validateUser(email, password):
    return True

@app.route("/signUp", methods=['POST'])
def signUp():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone_number = request.form['phone_number']
    company_name = request.form['company_name']
    company_size = request.form['company_size']
    print(fname)
    if email and password:

        # return json.dumps({'validation' : validateUser(email, password)})
        return render_template("login.html") 
    return  json.dumps({'validation' : False})


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()