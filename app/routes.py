import datetime
from flask import Blueprint, render_template, redirect, url_for, request, json, session, jsonify 
from app.models import User, Request, Admin
from flask_login import  UserMixin, login_user, current_user, login_required, logout_user
from app import db, login_manager

main = Blueprint('main', __name__,url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @login_manager.user_loader
# def load_admin(admin_id):
#     return Admin.query.get(int(admin_id))


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
      
        new_user = User(first_name=request.form['fname'], last_name=request.form['lname'], email=request.form['email'],
                         phone_number=request.form['phone_number'], password=request.form['password'], company_name=request.form['company_name'], company_size=request.form['company_size'] )
        
        User.add(new_user)

        return redirect('/')

    return render_template('register.html')

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
      
        if user and user.password == request.form['password']:
            session['user_id'] = user.id 
            login_user(user, remember=user.id)
        
            requests = Request.query.filter_by(user_id=user.id).all()
            return render_template('profile.html', user=user, requests=requests)
        
        return 'Invalid email or password'
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)  
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/get_user')
@login_required
def get_user():
    email = current_user.email
    user = User.query.get(email)
    return  render_template('user.html', user=user)

@main.route('/get_all_users', methods=['GET'])
@login_required
def get_all_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'email': user.email} for user in users]
    return render_template('users.html', users=user_list)


@main.route('/update_user/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
       
        user.email = request.json.get('email', user.email)
        user.save()

        user= User.query.get(user_id)
        return render_template('users.html', users=user)
    return 'User not found'

@main.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin = Admin.query.filter_by(email=request.form['email']).first()
        if admin and admin.password == request.form['password']:
                session['admin_id'] = admin.id 
                login_user(admin, remember=admin.id)

                users = User.query.all()
                requests = Request.query.all()

                return render_template('dashboard.html', users=users, requests=requests)
        return 'Invalid name or password'
    
    return render_template('admin_login.html')

@main.route('/create_request', methods=['GET', 'POST'])
@login_required
def create_request():
    print("current_user",current_user.id)
    user = User.query.get(current_user.id)
    if request.method == 'POST':
        user_id = current_user.id
        connection_type = request.form['connection_type']
        services = request.form['services']
        status = 'Pending'  
        date = datetime.datetime.now()  
        assigned_account_manager = None  
        verification_notes = None  
        description = request.form['description']

        new_request = Request(
            user_id=user_id,
            connection_type=connection_type,
            services=services,
            status=status,
            date=date,
            assigned_account_manager=assigned_account_manager,
            verification_notes=verification_notes,
            description=description
        )

        Request.add(new_request)
        print("////////////////////////",user.id)
        
        requests = Request.query.filter_by(user_id=user.id).all()
        print("///????????????????????????",requests)

        return render_template('profile.html', user=user, requests=requests)
    
    requests = Request.query.filter_by(user_id=user.id)
    return render_template('profile.html', user=user, requests=requests)

@main.route('/requests')
@login_required
def view_requests():
    if current_user.is_admin:  # Assuming you have an is_admin property in your Admin model
        requests = Request.query.all()
    else:
        requests = Request.query.filter_by(user_id=current_user.id).all()

    return render_template('view_requests.html', requests=requests)