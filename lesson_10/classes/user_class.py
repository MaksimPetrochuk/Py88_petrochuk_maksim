from exceptions import login_validation, new_value_validation, user_exceptions
from classes import data_storage_class
import json


class User:
    def __init__(self, name, password, age, key):
        self.name = name
        self.password = password
        self.age = age
        self.key = key

    @staticmethod
    def ask_name():
        return input('Input your username: ')

    @staticmethod
    def ask_password():
        return input('Input your password: ')

    @staticmethod
    def ask_n_check_age():
        while True:
            age = input('Input your age: ')
            if not age.isdigit():
                print('Error. Age must be an integer number. Try again.')
                continue
            return age

    @staticmethod
    def ask_key():
        return input('Input your key: ')

    @staticmethod
    def user_adding(name, password, age, key):
        user = User(name, password, age, key)
        user.save()

    def save(self, _delete=None):
        if _delete is not None:
            logins = data_storage_class.DataStorage.delete_changed_user(_delete.name)
        else:
            logins = data_storage_class.DataStorage.get_all_logins()
        logins.append({
            "name": self.name,
            "password": self.password,
            "age": self.age,
            "key": self.key
        })
        with open(data_storage_class.DataStorage.path_to_storage, 'w') as file:
            json.dump(logins, file, indent=' ')

    @staticmethod
    def auth_before_changes():
        check_logins = data_storage_class.DataStorage.turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            user = user_exceptions.UserExistenceError.find_user()
            if not user:
                continue
            else:
                return user
        return None

    @staticmethod
    def change_name():
        while True:
            user = User.auth_before_changes()
            if user:
                while True:
                    print('You need to enter your password in order to change your name.')
                    password = User.ask_password()
                    if user.password == password:
                        while True:
                            new_name = input('Set your new username: ')
                            if new_value_validation.PrevValueAsNewError.check_value(new_name, user.name) is None:
                                continue
                            if user_exceptions.UsernameIsTakenError.find_user(new_name) is None:
                                continue
                            if not login_validation.LoginValidation.check_name(new_name):
                                continue
                            else:
                                new_user = User(new_name, user.password, user.age, user.key)
                                new_user.save(user)
                                print('Successfully changed your name.')
                                break
                    else:
                        print('Incorrect password. Try again')
                        continue
                    break
            else:
                print('Error.')

    @staticmethod
    def change_age():
        user = User.auth_before_changes()
        if user:
            while True:
                print('You need to enter your password in order to change your age.')
                password = User.ask_password()
                if user.password == password:
                    while True:
                        new_age = input('Set your new age: ')
                        if new_value_validation.PrevValueAsNewError.check_value(new_age, user.age) is None:
                            continue
                        else:
                            new_user = User(user.name, user.password, new_age, user.key)
                            new_user.save(user)
                            print('Successfully changed your age.')
                            break
                else:
                    print('Incorrect password. Try again')
                    continue
                break
        else:
            print('Error.')

    @staticmethod
    def change_password():
        user = User.auth_before_changes()
        if user:
            while True:
                print('You need to enter your key in order to change your password.')
                key = User.ask_key()
                if user.key == key:
                    while True:
                        new_password = input('Set your new password: ')
                        if new_value_validation.PrevValueAsNewError.check_value(new_password, user.password) is None:
                            continue
                        else:
                            new_user = User(user.name, new_password, user.age, user.key)
                            new_user.save(user)
                            print('Successfully changed your password.')
                            break
                else:
                    print('Incorrect key. Try again')
                    continue
                break
        else:
            print('Error.')
