from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# User model for login and signup
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    groups = db.relationship('Group', backref='user', lazy=True)

# Group model to store group data
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expenses = db.relationship('Expense', backref='group', lazy=True)

# Expense model to store group expenses
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g. Food, Travel, etc.
    amount = db.Column(db.Float, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    paid_by = db.Column(db.String(150), nullable=False)
    split_type = db.Column(db.String(50), nullable=False)  # "Equal" or "Custom"
    # For custom split, store as JSON (e.g. {"user1": 50, "user2": 30})
    custom_split = db.Column(db.Text, nullable=True)
