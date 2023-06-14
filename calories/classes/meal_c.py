from databases import meal_db
import json


class Meal:
    def __init__(self, date, mass, product):
        self.date = date
        self.mass = mass
        self.prod = product

    def save(self):
        data = meal_db.DBMeals.get_all_meals()
        data.append({
            "date": str(self.date),
            "mass": self.mass,
            "product": self.prod
        })
        with open(meal_db.DBMeals.path, 'w') as file:
            json.dump(data, file, indent=' ')
