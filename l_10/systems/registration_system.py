from classes import user_class, data_storage_class
from exceptions import login_validation


class RegistrationSystem:
    @classmethod
    def registration(cls):
        while True:
            print("""
            WARNING! We are using our Format of usernames: username@hostname,
            where username consists of latin alphabet, digits, symbols such as in []:
            [! # % ' * + / = ? ^ _ ` { | } ~ -], space and a dot
            (dot can't be the first and the last symbol of the username and can't be repeated after another dot),
            hostname consists of 1 to 5 groups of latin alphabet, digits, symbol '-'
            (it can't be the first and the last symbol of group)
            which are separated by a dot and consist of 1 to 63 symbols.
            """)
            name = user_class.User.ask_name()
            user = data_storage_class.DataStorage.find_user_by_name(name)
            if user:
                print('Error. There is already a user with this name. Try again.')
                continue
            login_validation.LoginValidation.check_name(name)
            password = user_class.User.ask_password()
            age = user_class.User.ask_n_check_age()
            key = user_class.User.ask_key()
            user_class.User.user_adding(name, password, age, key)
            print(f'Registration completed. Your login: {name} - {password} .')
            break
