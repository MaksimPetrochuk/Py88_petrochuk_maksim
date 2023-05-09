from dataclasses import dataclass
import json


@dataclass
class DataStorage:
    path_to_storage: str = 'logins.json'


class User:
    def __init__(self, name, password, age, key):
        self.name = name
        self.password = password
        self.age = age
        self.key = key

    def save(self, _delete=None):
        if _delete is not None:
            logins = delete_changed_user(_delete.name)
        else:
            logins = get_all_logins()
        logins.append({
            "name": self.name,
            "password": self.password,
            "age": self.age,
            "key": self.key
        })
        with open(DataStorage.path_to_storage, 'w') as file:
            json.dump(logins, file, indent=' ')

    @staticmethod
    def change_name():
        check_logins = turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            print('What is your username?')
            name = ask_name()
            user = find_user_by_name(name)
            if not user:
                print('Error. There is no such user. Try again.')
                continue
            while True:
                print('You need to enter your password in order to change your name.')
                password = ask_password()
                if user.password == password:
                    while True:
                        new_name = input('Set your new username: ')
                        if new_name == user.name:
                            print('Error. New name must differ from previous. Try again.')
                            continue
                        if find_user_by_name(new_name):
                            print('Error. This username is already taken.')
                            continue
                        if not check_name(new_name):
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
            break

    @staticmethod
    def change_age():
        check_logins = turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            print('What is your username?')
            name = ask_name()
            user = find_user_by_name(name)
            if not user:
                print('Error. There is no such user. Try again.')
                continue
            while True:
                print('You need to enter your password in order to change your age.')
                password = ask_password()
                if user.password == password:
                    while True:
                        new_age = ask_n_check_age()
                        if new_age == user.age:
                            print('Error. New age must differ from previous. Try again.')
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
            break

    @staticmethod
    def change_password():
        check_logins = turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            print('What is your username?')
            name = ask_name()
            user = find_user_by_name(name)
            if not user:
                print('Error. There is no such user. Try again.')
                continue
            while True:
                print('You need to enter your key in order to change your password.')
                key = ask_key()
                if user.key == key:
                    while True:
                        new_password = ask_password()
                        if new_password == user.password:
                            print('Error. New password must differ from previous. Try again.')
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
            break


class AuthenticationSystem:
    @classmethod
    def authentication(cls):
        check_logins = turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            name = ask_name()
            user = find_user_by_name(name)
            if not user:
                print('Error. There is no such user. Try again.')
                continue
            password = ask_password()
            if user.password == password:
                print(f'Hello, {name}!')
                break
            else:
                print('Incorrect password. Try again.')
                continue
        return True


class RegistrationSystem:
    @classmethod
    def registration(cls):
        while True:
            name = ask_name()
            user = find_user_by_name(name)
            if user:
                print('Error. There is already a user with this name. Try again.')
                continue
            password = ask_password()
            age = ask_n_check_age()
            key = ask_key()
            user_adding(name, password, age, key)
            print(f'Registration completed. Your login: {name} - {password} .')
            break


def ask_name():
    return input('Input your username: ')


def check_name(name):
    if len(name) < 3 or len(name) > 15:
        print('Error. Username must be of 3 to 15 characters.')
        return False
    else:
        return name


def ask_password():
    return input('Input your password: ')


def ask_n_check_age():
    while True:
        age = input('Input your age: ')
        if not age.isdigit():
            print('Error. Age must be an integer number. Try again.')
            continue
        return age


def ask_key():
    return input('Input your key: ')


def get_all_logins():
    with open(DataStorage.path_to_storage, 'r') as file:
        logins = file.read()
        return [] if not logins else json.loads(logins)


def user_adding(name, password, age, key):
    user = User(name, password, age, key)
    user.save()


def turn_logins_into_class_user():
    logins = get_all_logins()
    result = []
    for obj in logins:
        name = obj["name"]
        password = obj["password"]
        age = obj["age"]
        key = obj["key"]
        user = User(name, password, age, key)
        result.append(user)
    return result


def delete_changed_user(name):
    result = get_all_logins()
    for user in result:
        if user["name"] == name:
            result.remove(user)
    return result


def find_user_by_name(name):
    users = turn_logins_into_class_user()
    for user in users:
        if user.name == name:
            return user


def change_option():
    while True:
        _option = input('Enter "n", or "a", or "p" to change your name, age or password, something else to exit: ')
        _action = menu_2.get(_option)
        if not _action:
            break
        _action()
        break


menu_1 = {
        'r': RegistrationSystem.registration,
        'a': AuthenticationSystem.authentication,
        'ch': change_option
    }
menu_2 = {
        'n': User.change_name,
        'a': User.change_age,
        'p': User.change_password
    }
while True:
    print('Enter "r" to registrate, "a" to authenticate, ', end='')
    print('"ch" to change your data, something else to exit: ', end='')
    option = input()
    action = menu_1.get(option)
    if not action:
        break
    action()
