# Первая часть ДЗ

def false():
    var = False
    return [int(var), int(not var), len(str(var)) + len(str(var))]

# Вторая часть ДЗ


names = ['name_1', 'name_2', 'name_3', 'name_4', 'name_5']
passwords = ['pass_1', 'pass_2', 'pass_3', 'pass_4', 'pass_5']


def get_name():
    print('Input your username:', end=' ')
    word = input()
    temp = check_name(word)
    return temp


def check_name(word):
    num = 1

    """
    Цикл перебора по списку имён, где выполняется поиск введённого имени
    и, в случае нахождения такового, оно возвращается вместе с порядковым номером.
    Случай ненахода (else): предлагается зарегестрировать несуществующего пользователя
    и в любом случае возвращается список [False, None] (для чего - объяснено дальше)
    """

    for obj in names:
        if obj == word:
            return [word, num]
        else:
            num += 1
            continue
    else:
        print('Error! There is no user with this name. Do you want to add new user? Send "Y" to do so.')
        option = input()
        if option == 'Y':
            print('Set your username:', end=' ')
            name = input()
            for obj in names:
                if obj == name:
                    print('Error! This name is already used.')
                    return [False, None]
                else:
                    continue
            names.append(name)
            print('Set your password:', end=' ')
            password = input()
            passwords.append(password)
        return [False, None]


def get_password():
    print('Input your password:', end=' ')
    word = input()
    temp = check_password(word)
    return temp


def check_password(word):
    num = 1

    """
    Цикл перебора по списку паролев, где выполняется поиск введённого пароля
    и, в случае нахождения такового, проверяет, чтобы он соответсвовал нужному имени
    по номеру в списке. В случае ненахода возвращается False (для чего - объяснено дальше)
    """

    for obj in passwords:
        if obj == word:
            if num == num_n:
                return True
            else:
                print('Authentication error! Try again.')
                return False
        else:
            num += 1
            continue
    else:
        print('Authentication error! Try again.')
        return False


_bool = False

"""
Цикл, выполняющий запрос имени до тех пор, пока не будет введено существующее
вместе с соответствующим ему паролем:
если имя не существует (т.е. False в списке [False, None]), то цикл запускается заново
если имя существует, но пароль введён неверный (False), то цикл перезапускается
если имя существует и введён верный пароль, то выводится приветствие и цикл заканчивается
"""

while _bool is False:
    word_n, num_n = get_name()
    if word_n is False:
        continue
    else:
        word_p = get_password()
        if word_p is False:
            continue
        else:
            print(f'Hello, {word_n}!')
            _bool = True
