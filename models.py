from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #Creates a column with a primary key
    username = db.Column(db.String(20), unique=True, nullable=False) #Creates a column with a unique constraint
    password = db.Column(db.String(60), nullable=False)
    shopping_list_items = db.relationship("ShoppingListItem", backref="user", lazy=True) #Creates a one-to-many relationship with the ShoppingListItem model

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False, unique=True)
    items = db.relationship('Item', backref='category', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False) #Creates a foreign key constraint
    shopping_list_items = db.relationship('ShoppingListItem', backref='item', lazy=True) #Creates a one-to-many relationship with the ShoppingListItem model

class ShoppingListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False) 
    checked = db.Column(db.Boolean, default=False) #Creates a column with a default value