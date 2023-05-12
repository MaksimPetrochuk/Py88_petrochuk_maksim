from classes import user_class, data_storage_class


class AuthenticationSystem:
    @classmethod
    def authentication(cls):
        check_logins = data_storage_class.DataStorage.turn_logins_into_class_user()
        while True:
            if not check_logins:
                print('There are no registered users. You should registrate.')
                break
            name = user_class.User.ask_name()
            user = data_storage_class.DataStorage.find_user_by_name(name)
            if not user:
                print('Error. There is no such user. Try again.')
                continue
            password = user_class.User.ask_password()
            if user.password == password:
                print(f'Hello, {name}!')
                break
            else:
                print('Incorrect password. Try again.')
                continue
        return True
