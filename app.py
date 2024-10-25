from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json
from models import db, User, Group, Expense

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route('/')
def index():
    if current_user.is_authenticated:
        groups = Group.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', groups=groups)
    return render_template('index.html')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Create Group Route
@app.route('/group', methods=['POST', 'GET'])
@login_required
def group():
    if request.method == 'POST':
        group_name = request.form['group_name']
        new_group = Group(name=group_name, user_id=current_user.id)
        db.session.add(new_group)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('group.html')

# Add Expense Route
@app.route('/add_expense/<group_id>', methods=['POST', 'GET'])
@login_required
def add_expense(group_id):
    group = Group.query.get(group_id)
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']
        amount = float(request.form['amount'])
        paid_by = request.form['paid_by']
        split_type = request.form['split_type']
        
        custom_split = None
        if split_type == 'Custom':
            custom_split = request.form['custom_split']  # Custom split in JSON format

        new_expense = Expense(description=description, category=category, amount=amount,
                              group_id=group.id, paid_by=paid_by, split_type=split_type,
                              custom_split=json.dumps(custom_split))
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html', group=group)

# Calculate Split Route
@app.route('/calculate/<group_id>')
@login_required
def calculate(group_id):
    group = Group.query.get(group_id)
    expenses = Expense.query.filter_by(group_id=group_id).all()
    
    # Logic to calculate the split
    total_expense = sum(expense.amount for expense in expenses)
    num_people = len(set(expense.paid_by for expense in expenses))
    
    result = []
    for expense in expenses:
        if expense.split_type == 'Equal':
            split_amount = total_expense / num_people
            result.append((expense.paid_by, expense.amount - split_amount))
        elif expense.split_type == 'Custom':
            custom_split = json.loads(expense.custom_split)
            for person, amount in custom_split.items():
                result.append((person, amount))
    
    return render_template('result.html', group=group, result=result, total_expense=total_expense)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

