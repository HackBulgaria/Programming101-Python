class HasAtleastOneSymbolValidation:
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

validator = PasswordValidator()
validator.add_validation(LengthValidation(8))
validator.add_validation(HasAtleastOneSymbolValidation(['$']))
validator.add_validation(lambda string: string.count("&") == 2)
