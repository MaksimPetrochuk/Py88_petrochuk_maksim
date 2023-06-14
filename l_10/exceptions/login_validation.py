import sys
import re


class LoginValidation(Exception):
    @staticmethod
    def check_name(name):
        try:
            assert re.match("^[a-zA-Z0-9!# %'*+/=?^_`{|}~-]+"
                            "((\\.[a-zA-Z0-9!# %'*+/=?^_`{|}~-]+)+)?@"
                            "(\\.?[a-zA-Z0-9]"
                            "([a-zA-Z0-9-]{,61}"
                            "[a-zA-Z0-9])?){,5}$", name) is not None
            return name
        except AssertionError:
            print('LoginValidationError. Username should meet the Format.')
            sys.exit()
