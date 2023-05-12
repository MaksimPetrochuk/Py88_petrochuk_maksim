import sys


class LoginValidation(Exception):
    @staticmethod
    def check_name(name):
        try:
            assert len(name) < 3
            assert len(name) > 15
            return name
        except AssertionError:
            print('LoginValidationError: Username must be of 3 to 15 characters.')
            sys.exit()
