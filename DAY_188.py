class Wallet:
    def __init__(self, money):
        self.money = money

    def __add__(self, other):
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"Wallet Balance: ₹{self.money}"

wallet1 = Wallet(500)
wallet2 = Wallet(1000)
wallet3 = Wallet(1000)

print(wallet1 + wallet2 + wallet3)