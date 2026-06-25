class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # Private Variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance: {self.__balance}")


account1 = BankAccount("Samarth", 5000)

account1.show_balance()

account1.deposit(1000)
account1.show_balance()

account1.withdraw(2000)
account1.show_balance()

# Try this:
# print(account1.__balance)