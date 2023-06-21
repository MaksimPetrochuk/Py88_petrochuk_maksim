from databases.product_database import DBProducts
from systems.isdigit_validation import check
from classes.product_class import Product


class AddingProductSystem:
    @classmethod
    def adding(cls):
        protein = None
        fats = None
        carbohydrates = None
        kcal = None
        while True:
            name = input("Input name of the product: ")
            product = DBProducts.find_product_by_name(name)
            if product:
                print("Error. There is already a product with this name. Try again.")
                continue
            break
        _bool = True
        while _bool:
            protein = input("Input amount of protein in it for 100 grams of product: ")
            protein = check(protein)
            if protein is False:
                continue
            else:
                _bool = False
        _bool = True
        while _bool:
            fats = input("Input amount of fats in it for 100 grams of product: ")
            fats = check(fats)
            if fats is False:
                continue
            else:
                _bool = False
        _bool = True
        while _bool:
            carbohydrates = input("Input amount of carbohydrates in it for 100 grams of product: ")
            carbohydrates = check(carbohydrates)
            if carbohydrates is False:
                continue
            else:
                _bool = False
        _bool = True
        while _bool:
            kcal = input("Input amount of kilocalories in it for 100 grams of product: ")
            kcal = check(kcal)
            if kcal is False:
                continue
            else:
                _bool = False
        product = Product(name, protein, fats, carbohydrates, kcal)
        DBProducts.save(product)
