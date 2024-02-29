from models import db, Restaurant, Pizza, Restaurant_pizza
from app import app

def seed():
    with app.app_context():
        Pizza.query.delete()
        Restaurant_pizza.query.delete()
        Restaurant.query.delete()
        
        # Create some pizzas
        margherita = Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil")
        pepperoni = Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni")
        hawaiian = Pizza(name="Hawaiian", ingredients="Tomato sauce, mozzarella, ham, pineapple")
        
        # Add pizzas to the session
        db.session.add(margherita)
        db.session.add(pepperoni)
        db.session.add(hawaiian)
        
        # Commit the changes
        db.session.commit()
        
        # Create some restaurants
        restaurant1 = Restaurant(name="Pizza Place", address="123 Main St")
        restaurant2 = Restaurant(name="Italian Restaurant", address="456 Elm St")
        
        # Add restaurants to the session
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        
        # Commit the changes
        db.session.commit()
        
        # Create some restaurant_pizzas
        restaurant_pizza1 = Restaurant_pizza(restaurant=restaurant1, pizza=margherita, price=10.99)
        restaurant_pizza2 = Restaurant_pizza(restaurant=restaurant1, pizza=pepperoni, price=12.99)
        restaurant_pizza3 = Restaurant_pizza(restaurant=restaurant2, pizza=hawaiian, price=11.99)
        
        # Add restaurant_pizzas to the session
        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)
        db.session.add(restaurant_pizza3)
        
        # Commit the changes
        db.session.commit()

if __name__ == "__main__":
    seed()
