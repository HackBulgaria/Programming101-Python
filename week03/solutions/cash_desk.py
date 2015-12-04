class CashDesk:
    def __init__(self):
        self.cash = []

    def take_money(self, amount):
        self.cash.append(amount)

    def total(self):
        return sum([obj.total() for obj in self.cash])
