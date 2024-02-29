# app/routes.py
from flask_migrate import Migrate
from flask import Flask, jsonify, request

from models import db, Restaurant, Pizza, Restaurant_pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [
        {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}
        for restaurant in restaurants
    ]
    return jsonify(restaurant_list)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_pizzas = Restaurant_pizza.query.filter_by(restaurant_id=id).all()
        pizza_list = [
            {"id": rp.pizza.id, "name": rp.pizza.name, "ingredients": rp.pizza.ingredients, "price": rp.price}
            for rp in restaurant_pizzas
        ]
        return jsonify({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizza_list})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}
        for pizza in pizzas
    ]
    return jsonify(pizza_list)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not (price and pizza_id and restaurant_id):
        return jsonify({"errors": ["price, pizza_id, and restaurant_id are required"]}), 400

    try:
        restaurant_pizza = Restaurant_pizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 500
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
