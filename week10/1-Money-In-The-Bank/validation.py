import string


class AtleastOneSymbol:
    def __init__(self, symbols):
        self.__symbols = symbols

    def __call__(self, string):
        return any([ch in self.__symbols for ch in string])


class LengthValidation:
    def __init__(self, length):
        self.__length = length

    def __call__(self, string):
        return len(string) >= self.__length


class PasswordValidator:
    def __init__(self):
        self.__validators = []

    def is_valid(self, password):
        return all([v(password) for v in self.__validators])

    def add_validation(self, validator):
        self.__validators.append(validator)
        return self


CAPITAL_LETTERS = list(string.ascii_uppercase)
NUMBERS = list("1234567890")
SPECIAL_SYMBOLS = list(string.punctuation)


def get_validator(username):
    validator = PasswordValidator()
    validator\
        .add_validation(LengthValidation(9))\
        .add_validation(AtleastOneSymbol(CAPITAL_LETTERS))\
        .add_validation(AtleastOneSymbol(NUMBERS))\
        .add_validation(AtleastOneSymbol(SPECIAL_SYMBOLS))\
        .add_validation(lambda pwd: username.lower() not in pwd.lower())
    return validator


class StrongPasswordException(Exception):
    pass
