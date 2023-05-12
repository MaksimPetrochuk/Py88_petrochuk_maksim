from classes import user_class, data_storage_class


class UserExistenceError(Exception):
    @staticmethod
    def find_user():
        try:
            print('What is your username?')
            name = user_class.User.ask_name()
            user = data_storage_class.DataStorage.find_user_by_name(name)
            assert user is not None
            return user
        except AssertionError:
            print('UserExistenceError. There is no such user. Try again.')
            return None


class UsernameIsTakenError(Exception):
    @staticmethod
    def find_user(name):
        try:
            user = data_storage_class.DataStorage.find_user_by_name(name)
            assert user is None
            return name
        except AssertionError:
            print('UsernameIsTakenError. This username is already taken. Try again.')
            return None
