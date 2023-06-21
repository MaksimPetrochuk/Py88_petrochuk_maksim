from dataclasses import dataclass
import json
import sys

from classes.meal_class import Meal


path_to_project = sys.path
path_to_file = path_to_project[1] + "/databases/Meals.json"


@dataclass
class DBMeals:
    path: str = path_to_file

    @classmethod
    def get_all_meals(cls):
        while True:
            try:
                with open(cls.path, "r") as file:
                    data = file.read()
                    return [] if not data else json.loads(data)
            except OSError:
                print("File with logins do not exists so it has been created.")
                with open(cls.path, "w"):
                    pass

    @staticmethod
    def convert_all_meals_to_meal_class_instances():
        data = DBMeals.get_all_meals()
        meals = []
        for obj in data:
            date = obj["date"]
            grams = obj["grams"]
            product = obj["product"]
            meal = Meal(date, grams, product)
            meals.append(meal)
        return meals

    @staticmethod
    def save(meal):
        data = DBMeals.get_all_meals()
        data.append({
            "date": str(meal.date_of_consumption),
            "grams": meal.grams,
            "product": meal.product_name
        })
        with open(DBMeals.path, 'w') as file:
            json.dump(data, file, indent=' ')
