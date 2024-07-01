class Bank:
    def __init__(self, amounts):
        self._amounts = amounts.copy()

    def transfer(self, sender, receiver, yen):
        self._amounts[sender] -= yen
        self._amounts[receiver] += yen

    def withdraw(self, name, yen):
        if self._amounts[name] < yen:
            return None
        self._amounts[name] -= yen
        return self._amounts[name]

bank = Bank({
    "bob": 1234
})

balance = bank.withdraw("bob", 234)
print(balance)  # 1000
balance = bank.withdraw("bob", 9999)
print(balance)  # None
