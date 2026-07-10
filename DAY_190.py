class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Added Successfully")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def __str__(self):
        return f"Account Holder : {self.name}\nBalance : ₹{self.balance}"

    def __eq__(self, other):
        return self.name == other.name and self.balance == other.balance

    def __add__(self, other):
        return BankAccount("Joint Account", self.balance + other.balance)

account1 = BankAccount("Samarth", 5000)
account2 = BankAccount("Alex", 3000)

account1.deposit(1000)
account2.withdraw(500)

print(account1 == account2)

joint = account1 + account2
print("\nJoint Account Details:")
print(joint)