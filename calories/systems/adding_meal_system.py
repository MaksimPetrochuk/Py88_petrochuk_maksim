from databases import product_db
from classes import meal_c
from datetime import datetime


class AddingMealSystem:
    @classmethod
    def ams(cls):
        _str = '.0123456789'
        mass = ''
        date = datetime.now()
        while True:
            product = input("Product: ")
            if not product_db.DBProducts.find_product_by_name(product):
                print('There is no such product in DB. Try again.')
                continue
            break
        _bool = True
        while _bool:
            counter = 0
            mass = input("Input mass of the meal: ")
            for char in mass:
                if char not in _str:
                    print('Error. You must enter a digit.')
                    break
                if char == '.':
                    counter += 1
                if counter > 1:
                    print('Error. You must enter a digit.')
                    break
                else:
                    _bool = False
        meal = meal_c.Meal(str(date), mass, product)
        meal_c.Meal.save(meal)
