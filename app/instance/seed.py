from faker import Faker
from flask import Flask
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, Restaurant, Pizza, Restaurant_Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        engine = db.engine
        Session = sessionmaker(bind=engine)
        session = Session()

        session.query(Pizza).delete()
        session.query(Restaurant).delete()
        session.query(Restaurant_Pizza).delete()
        session.commit()

        pizzas_list = ['pepperoni', 'hawaiian', 'meat-deluxe', 'bacon-macon', 'meat-lovers', 'chicken tikka']
        ingredient_lists = [
            'cheese, tomato sauce, pepperoni',
            'mozzarella, tomato, basil, olive oil',
            'cheddar, broccoli, chicken, ranch sauce',
            'feta, spinach, black olives, garlic',
            'gouda, ham, pineapple, bbq sauce',
            'parmesan, tomato sauce, italian sausage, green peppers',
            'mozzarella, tomato sauce, mushrooms, onions',
            'provolone, alfredo sauce, bacon, chicken',
            'gorgonzola, figs, prosciutto, balsamic glaze',
            'blue cheese, steak strips, caramelized onions, horseradish sauce',
            'cheddar, chili, jalapenos, sour cream',
            'pepper jack, buffalo chicken, ranch dressing, celery',
            'swiss, ham, dijon mustard, pickles',
            'cream cheese, smoked salmon, red onion, capers',
        ]
        fake = Faker()

        restaurants = []
        for _ in range(random.randint(1, 12)):
            restaurant = Restaurant(
                address=fake.unique.sentence()
            )
            restaurants.append(restaurant)

        session.bulk_save_objects(restaurants)
        session.commit()

        pizzas = []
        for _ in range(random.randint(1, 12)):
            pizza = Pizza(
                name=random.choice(pizzas_list),
                ingredients=random.choice(ingredient_lists),
                created_at=fake.date_time_this_decade(),
                updated_at=fake.date_time_this_month()
            )
            pizzas.append(pizza)

        session.bulk_save_objects(pizzas)
        session.commit()

        restaurant_pizzas = []
        for _ in range(random.randint(1, 12)):
            pizza = random.choice(pizzas)
            restaurant = random.choice(restaurants)
            if pizza and restaurant:  
                restaurant_pizza = Restaurant_Pizza(
                    pizza_id=pizza.id,
                    restaurant_id=restaurant.id,
                    price=fake.random_int(min=5, max=20),
                    created_at=fake.date_time_this_decade(),
                    updated_at=fake.date_time_this_month()
                )
                restaurant_pizzas.append(restaurant_pizza)

        session.bulk_save_objects(restaurant_pizzas)
        session.commit()

        session.close()