def check(number):
    try:
        number = float(number)
        assert number >= 0
        return number
    except TypeError:
        print("Error. You must enter a digit.")
        return False
    except AssertionError:
        print("Error. Digit must be not negative.")
        return False
