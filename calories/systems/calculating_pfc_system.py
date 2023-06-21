from datetime import datetime, timedelta

from databases.product_database import DBProducts
from databases.meal_database import DBMeals


MASS = 100  # all PFC and kcal are calculated for 100 grams of product


class Calculating:

    @staticmethod
    def ask_period_of_calculation():
        menu = {
            "1": 1,
            "3": 3,
            "7": 7,
            "30": 30
        }
        while True:
            ask_period = input("Input period of calculation (1, 3, 7 or 30 days): ")
            period = menu.get(ask_period)
            if not period:
                print("Input 1, 3, 7 or 30 to calculate your PFC consumption in this period!")
                continue
            return period

    @staticmethod
    def calculator(variable, mass):
        return variable * mass / MASS

    @staticmethod
    def calculate():
        period = Calculating.ask_period_of_calculation()
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
                product_name = meal["product"]
                product = DBProducts.find_product_by_name(product_name)

                meal_mass = float(meal["grams"])

                meal_protein = float(product.protein)
                meal_fats = float(product.fats)
                meal_carbohydrates = float(product.carbohydrates)
                meal_calories = float(product.kcal)

                protein += Calculating.calculator(meal_protein, meal_mass)
                fats += Calculating.calculator(meal_fats, meal_mass)
                carbohydrates += Calculating.calculator(meal_carbohydrates, meal_mass)
                calories += Calculating.calculator(meal_calories, meal_mass)
        print(f"You have eaten {protein} of protein, {fats} of fats, "
              f"{carbohydrates} of carbohydrates with total of {calories} kilocalories")
        return True
