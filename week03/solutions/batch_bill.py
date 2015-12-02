class BatchBill:
    def __init__(self, bills):
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def __int__(self):
        return sum([bill.get_amount() for bill in self._bills])

    def total(self):
        return int(self)
