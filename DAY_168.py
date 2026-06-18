class BankAccount:
    total_account = 0

    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance   
        self.account_number = account_number
        BankAccount.total_account += 1

    def showDetails(self):
        print(f"Account Holder: {self.account_holder}\n"
              f"Account Number: {self.account_number}\n"
              f"Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn New balance: {self.balance}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if self.balance < amount:
            print("Insufficient funds for transfer.")
            return
        
        self.balance -= amount
        other_account.balance += amount
        print(f"Transferred {amount} from {self.account_holder} "
              f"to {other_account.account_holder}.")

s = BankAccount("Samarth", 5000, 1)
s1 = BankAccount("Bob", 9000, 2)

s.showDetails()
s1.showDetails()

s.transfer(s1, 1000)

s.check_balance()  
s1.check_balance()  
