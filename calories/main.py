from systems.adding_product_system import AddingProductSystem
from systems.adding_meal_system import AddingMealSystem
from systems.calculating_pfc_system import Calculating


class Program:
    @staticmethod
    def process():
        menu = {
            "product": AddingProductSystem.adding,
            "meal": AddingMealSystem.adding,
            "amount": Calculating.calculate
        }
        while True:
            print("Enter 'product' to add new product, 'meal' to add meal, "
                  "'amount' to calculate amount of PFC and Kcal:", end=' ')
            option = input()
            action = menu.get(option)
            if not action:
                break
            action()


Program.process()
