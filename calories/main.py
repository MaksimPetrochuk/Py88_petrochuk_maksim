from systems import adding_product_system, adding_meal_system
from databases import meal_db


class Program:
    @staticmethod
    def process():
        menu = {
            'product': adding_product_system.AddingProductSystem.aps,
            'meal': adding_meal_system.AddingMealSystem.ams,
            'amount': meal_db.DBMeals.calc
        }
        while True:
            print('Enter "product" to add new product, "meal" to add meal, ', end='')
            print('"amount" to calculate amount of PFC and Kcal: ', end='')
            option = input()
            action = menu.get(option)
            if not action:
                break
            action()


Program.process()
