class BankAccount:
    def __init__(self, name, start_balance, currency):
        if start_balance < 0:
            raise ValueError("Start balance must be >= 0")

        self.__name = str(name)
        self.__balance = start_balance
        self.__currency = str(currency)
        self.__history = []
        self.__make_history("Account was created")

    def __make_history(self, event):
        self.__history.append(event)

    def __int__(self):
        self.__make_history("__int__ check -> {}{}"
                            .format(self.__balance, self.__currency))
        return self.__balance

    def __str__(self):
        return "Bank account for {} with balance of {}{}"\
            .format(self.__name, self.__balance, self.__currency)

    def holder(self):
        return self.__name

    def currency(self):
        return self.__currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative money.")

        self.__balance += amount
        self.__make_history("Deposited {}{}".format(amount, self.__currency))

    def balance(self):
        self.__make_history("Balance check -> {}{}"
                            .format(self.__balance, self.__currency))

        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__make_history("{}{} was withdrawed"
                                .format(amount, self.__currency))
            return True

        return False

    def history(self):
        return self.__history
