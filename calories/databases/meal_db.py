from databases import product_db
from classes import meal_c
from dataclasses import dataclass
from datetime import datetime, timedelta
import json


@dataclass
class DBMeals:
    path: str = '/home/mk/pp_tms/Py_88_maksim_petrochuk/calories/databases/Meals.json'

    @classmethod
    def get_all_meals(cls):
        while True:
            try:
                with open(cls.path, 'r') as file:
                    data = file.read()
                    return [] if not data else json.loads(data)
            except OSError:
                print('File with logins do not exists so it has been created.')
                with open(cls.path, 'w'):
                    pass

    @staticmethod
    def turn_into_class_meal():
        data = DBMeals.get_all_meals()
        meals = []
        for obj in data:
            date = obj["date"]
            mass = obj["mass"]
            product = obj["product"]
            meal = meal_c.Meal(date, mass, product)
            meals.append(meal)
        return meals

    @staticmethod
    def ask_period():
        menu = {
            '1': 1,
            '3': 3,
            '7': 7,
            '30': 30
        }
        while True:
            period = input("Input period of calculation (1, 3, 7 or 30 days): ")
            action = menu.get(period)
            if not action:
                print('"1" or "3" or "7" or "30"!')
                continue
            return int(period)

    @staticmethod
    def calc():
        period = DBMeals.ask_period()
        protein = 0
        fats = 0
        carbohydrates = 0
        calories = 0
        meals = DBMeals.get_all_meals()
        time = datetime.now() - timedelta(days=period)
        for meal in meals:
            year, month, day = int(meal["date"][:4]), int(meal["date"][5:7]), int(meal["date"][8:10])
            hour, minute = int(meal["date"][11:13]), int(meal["date"][14:16])
            if datetime(year, month, day, hour, minute) > time:
                name = meal["product"]
                product = product_db.DBProducts.find_product_by_name(name)
                protein += float(product.prot) * float(meal["mass"]) / 100
                fats += float(product.fats) * float(meal["mass"]) / 100
                carbohydrates += float(product.carb) * float(meal["mass"]) / 100
                calories += float(product.cal) * float(meal["mass"]) / 100
        print(f'You have eaten {protein} of protein, {fats} of fats', end=' ')
        print(f'{carbohydrates} of carbohydrates with total of {calories} kilocalories')
