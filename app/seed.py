from app import app
from models import Restaurant, Pizza, Restaurant_Pizza, db  # corrected the import

def seed_data():
    with app.app_context():
        Restaurant.query.delete()
        Restaurant_Pizza.query.delete()
        Pizza.query.delete()
        # Create restaurants
        restaurants_data = [
            {'name': 'Pizza Hut', 'address': '123 Main St'},
            {'name': 'Domino\'s Pizza', 'address': '456 Elm St'},
            {'name': 'Papa John\'s', 'address': '789 Oak St'},
            {'name': 'Little Caesars', 'address': '321 Pine St'},
            {'name': 'Pizza Express', 'address': '654 Cedar St'}
        ]
        for data in restaurants_data:
            restaurant = Restaurant(**data)
            db.session.add(restaurant)
        db.session.commit()

        # Create pizzas
        pizzas_data = [
            {'name': 'Cheese Pizza', 'ingredients': 'Cheese, Tomato Sauce'},
            {'name': 'Pepperoni Pizza', 'ingredients': 'Pepperoni, Cheese, Tomato Sauce'},
            {'name': 'Vegetarian Pizza', 'ingredients': 'Mushrooms, Peppers, Onions, Cheese, Tomato Sauce'},
            {'name': 'Hawaiian Pizza', 'ingredients': 'Ham, Pineapple, Cheese, Tomato Sauce'},
            {'name': 'Meat Lovers Pizza', 'ingredients': 'Pepperoni, Sausage, Bacon, Ham, Cheese, Tomato Sauce'}
        ]
        for data in pizzas_data:
            pizza = Pizza(**data)
            db.session.add(pizza)
        db.session.commit()

        # Create restaurant pizzas
        restaurant_pizzas_data = [
            {'restaurant_id': 1, 'pizza_id': 1},
            {'restaurant_id': 1, 'pizza_id': 2},
            {'restaurant_id': 2, 'pizza_id': 1},
            {'restaurant_id': 2, 'pizza_id': 3},
            {'restaurant_id': 3, 'pizza_id': 2},
            {'restaurant_id': 3, 'pizza_id': 4},
            {'restaurant_id': 4, 'pizza_id': 3},
            {'restaurant_id': 4, 'pizza_id': 5},
            {'restaurant_id': 5, 'pizza_id': 1},
            {'restaurant_id': 5, 'pizza_id': 5}
        ]
        for data in restaurant_pizzas_data:
            restaurant_pizza = Restaurant_Pizza(**data)  # corrected the class name
            db.session.add(restaurant_pizza)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
