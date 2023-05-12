from classes import user_class, data_storage_class
from exceptions import login_validation


class RegistrationSystem:
    @classmethod
    def registration(cls):
        while True:
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
