from databases import product_db
import json


class Product:
    def __init__(self, name, protein, fats, carbohydrates, calories):
        self.name = name
        self.prot = protein
        self.fats = fats
        self.carb = carbohydrates
        self.cal = calories

    def save(self):
        data = product_db.DBProducts.get_all_products()
        data.append({
            "name": self.name,
            "protein": self.prot,
            "fats": self.fats,
            "carbohydrates": self.carb,
            "calories": self.cal
        })
        with open(product_db.DBProducts.path, 'w') as file:
            json.dump(data, file, indent=' ')
