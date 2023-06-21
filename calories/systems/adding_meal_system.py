from databases.product_database import DBProducts
from databases.meal_database import DBMeals
from systems.isdigit_validation import check
from classes.meal_class import Meal
from datetime import datetime


class AddingMealSystem:
    @classmethod
    def adding(cls):
        grams = None
        date = datetime.now()
        while True:
            product = input("Product name: ")
            if not DBProducts.find_product_by_name(product):
                print("There is no such product in DB. Try again.")
                continue
            break
        _bool = True
        while _bool:
            grams = input("Input mass of the meal in grams: ")
            grams = check(grams)
            if grams is False:
                continue
            else:
                _bool = False
        meal = Meal(str(date), str(grams), product)
        DBMeals.save(meal)
