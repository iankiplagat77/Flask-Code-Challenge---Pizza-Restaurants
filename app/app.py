from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validates, ValidationError
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id', name='fk_pizza_id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', name='fk_restaurant_id'), nullable=False)

    @validates('price')
    def validate_price(self, key, value):
        if not 1 <= value <= 30:
            raise ValidationError('Price must be between 1 and 30.')
        return value
