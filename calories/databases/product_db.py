from dataclasses import dataclass
from classes import product_c
import json


@dataclass
class DBProducts:
    path: str = '/home/mk/pp_tms/Py_88_maksim_petrochuk/calories/databases/Products.json'

    @classmethod
    def get_all_products(cls):
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
    def turn_into_class_product():
        data = DBProducts.get_all_products()
        products = []
        for obj in data:
            name = obj["name"]
            protein = obj["protein"]
            fats = obj["fats"]
            carbohydrates = obj["carbohydrates"]
            calories = obj["calories"]
            product = product_c.Product(name, protein, fats, carbohydrates, calories)
            products.append(product)
        return products

    @staticmethod
    def find_product_by_name(name):
        products = DBProducts.turn_into_class_product()
        for product in products:
            if product.name == name:
                return product
