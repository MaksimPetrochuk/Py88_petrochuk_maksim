from dataclasses import dataclass
import json
import sys

from classes.product_class import Product


path_to_project = sys.path
path_to_file = path_to_project[1] + "/databases/Products.json"


@dataclass
class DBProducts:
    path: str = path_to_file

    @classmethod
    def get_all_products(cls):
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
    def turn_into_class_product():
        data = DBProducts.get_all_products()
        products = []
        for obj in data:
            name = obj["name"]
            protein = obj["protein"]
            fats = obj["fats"]
            carbohydrates = obj["carbohydrates"]
            calories = obj["calories"]
            product = Product(name, protein, fats, carbohydrates, calories)
            products.append(product)
        return products

    @staticmethod
    def find_product_by_name(name):
        products = DBProducts.turn_into_class_product()
        for product in products:
            if product.name == name:
                return product

    @staticmethod
    def save(product):
        data = DBProducts.get_all_products()
        data.append({
            "name": product.name,
            "protein": product.protein,
            "fats": product.fats,
            "carbohydrates": product.carbohydrates,
            "calories": product.kcal
        })
        with open(DBProducts.path, 'w') as file:
            json.dump(data, file, indent=' ')
