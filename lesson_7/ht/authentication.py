import json


def get_name():
    print('Input your username:', end=' ')
    word = input()
    temp = check_name(word)
    return temp


def check_name(word):
    with open('logins.json', 'r') as log:
        data = json.load(log)
    if word in data:
        print('This username exists.')
        return word
    else:
        print('Error. There is no user with this name.')
        return False


def get_password():
    print('Input your password:', end=' ')
    word = str(input())
    temp = check_password(word)
    return temp


def check_password(word):
    with open('logins.json', 'r') as log:
        data = json.load(log)
        for obj in data:
            if data[obj] == word:
                return True
        else:
            print('Incorrect password. Try again.')
            return False


def registration():
    with open('logins.json', 'r') as log:
        data = json.load(log)
        while True:
            print('Set your username:', end=' ')
            name = str(input())
            temp = len(name)
            if temp > 15 or temp < 2:
                print('Error. Name must consist of 2 to 15 symbols.')
                continue
            if name in data:
                print('Error. This name is already used.')
                continue
            print('This username is available. Set your password:', end=' ')
            password = str(input())
            data[name] = password
            with open('logins.json', 'w') as logins:
                json.dump(data, logins, indent='')
            print(f'Registration completed successfully. Your login: {name}: {password}.')
            break


print('You want to register or complete authentication? Send "r" to register, "a" to authenticate.')
option = input()
while True:
    if option == 'a':
        word_n = get_name()
        while True:
            word_p = get_password()
            if word_p is False:
                continue
            else:
                print(f'Hello, {word_n}!')
                break
    if option == 'r':
        registration()
        break
    else:
        print('Incorrect input. Try again. Send "r" to register, "a" to authenticate.')
        option = input()
        continue
