import json


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        logins = get_all_logins()
        logins.update({self.name: self.password})
        with open('logins.json', 'w') as file:
            json.dump(logins, file, indent=' ')


def ask_name():
    return input('Input your username: ')


def ask_password():
    return input('Input your password: ')


def get_all_logins():
    with open('logins.json', 'r') as file:
        logins = file.read()
        return {} if not logins else json.loads(logins)


def user_adding(name, password):
    user = User(name, password)
    user.save()


def class_user_maker():
    logins = get_all_logins()
    result = []
    for name in logins:
        user = User(name, logins[name])
        result.append(user)
    return result


def find_user_by_name(word):
    users = class_user_maker()
    for user in users:
        if user.name == word:
            return user


def authentication():
    while True:
        check_engine = class_user_maker()
        if not check_engine:
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


def registration():
    while True:
        name = ask_name()
        user = find_user_by_name(name)
        if user:
            print('Error. There is already a user with this name. Try again.')
            continue
        else:
            password = ask_password()
            user_adding(name, password)
            print(f'Registration completed. Your login: {name} - {password} .')
            break


while True:
    option = input('Enter "r" to registrate, "a" to authenticate, something else to exit: ')
    menu = {
        'r': registration,
        'a': authentication
    }
    action = menu.get(option)
    if not action:
        break
    action()
