from classes import user_class
from systems import authentication_system, registration_system


class Program:
    @staticmethod
    def process():
        menu_1 = {
            'r': registration_system.RegistrationSystem.registration,
            'a': authentication_system.AuthenticationSystem.authentication,
            'ch': Program.change_option
        }
        while True:
            print('Enter "r" to registrate, "a" to authenticate, ', end='')
            print('"ch" to change your data, something else to exit: ', end='')
            option = input()
            action = menu_1.get(option)
            if not action:
                break
            action()

    @staticmethod
    def change_option():
        menu_2 = {
            'n': user_class.User.change_name,
            'a': user_class.User.change_age,
            'p': user_class.User.change_password
        }

        while True:
            option = input('Enter "n", or "a", or "p" to change your name, age or password, something else to exit: ')
            action = menu_2.get(option)
            if not action:
                break
            action()
            break
