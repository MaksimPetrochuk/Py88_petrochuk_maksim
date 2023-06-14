from databases import product_db
from classes import product_c


class AddingProductSystem:
    @classmethod
    def aps(cls):
        _str = '.0123456789'
        prot = ''
        fats = ''
        carb = ''
        cal = ''
        while True:
            name = input("Input name of the product: ")
            product = product_db.DBProducts.find_product_by_name(name)
            if product:
                print('Error. There is already a product with this name. Try again.')
                continue
            break
        _bool = True
        while _bool:
            counter = 0
            prot = input("Input amount of protein in it: ")
            for char in prot:
                if char not in _str:
                    print('Error. You must enter a digit.')
                    break
                if char == '.':
                    counter += 1
                if counter > 1:
                    print('Error. You must enter a digit.')
                    break
                else:
                    _bool = False
        _bool = True
        while _bool:
            counter = 0
            fats = input("Input amount of fats in it: ")
            for char in fats:
                if char not in _str:
                    print('Error. You must enter a digit.')
                    break
                if char == '.':
                    counter += 1
                if counter > 1:
                    print('Error. You must enter a digit.')
                    break
                else:
                    _bool = False
        _bool = True
        while _bool:
            counter = 0
            carb = input("Input amount of carbohydrates in it: ")
            for char in carb:
                if char not in _str:
                    print('Error. You must enter a digit.')
                    break
                if char == '.':
                    counter += 1
                if counter > 1:
                    print('Error. You must enter a digit.')
                    break
                else:
                    _bool = False
        _bool = True
        while _bool:
            counter = 0
            cal = input("Input amount of kilocalories in it: ")
            for char in cal:
                if char not in _str:
                    print('Error. You must enter a digit.')
                    break
                if char == '.':
                    counter += 1
                if counter > 1:
                    print('Error. You must enter a digit.')
                    break
                else:
                    _bool = False
        product = product_c.Product(name, prot, fats, carb, cal)
        product_c.Product.save(product)
