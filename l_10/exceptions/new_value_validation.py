class PrevValueAsNewError(Exception):
    @staticmethod
    def check_value(new_val, prev_val):
        try:
            assert new_val != prev_val
            return new_val
        except AssertionError:
            print('PrevValueAsNewError. New value must differ from previous. Try again.')
            return None
