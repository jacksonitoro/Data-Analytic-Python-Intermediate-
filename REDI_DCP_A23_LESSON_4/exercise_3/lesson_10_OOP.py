class Bank_Account:
    def __init__(self):
        self.balance = 0 #initial account balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print(f"Invalid deposit amount. Try again")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        
        elif amount <= 0:
            print("Invalid amount. Please try again with correct amount")

        else:
            print("Insufficient balance. Please Withdrawal not possible")

account1 = Bank_Account()
account2 = Bank_Account()
print(f"Is account1 an instance of Bank_Account? {isinstance(account1, Bank_Account)}")
print(f"Is account1 an instance of Bank_Account? {isinstance(account2, Bank_Account)}")



account1.deposit(1000)
account1.withdraw(400)
    

account2.deposit(500)
account2.withdraw(700)


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Creating instances of BankAccount
account1 = BankAccount()
account2 = BankAccount()

# Checking if instances are of the BankAccount class
print(isinstance(account1, BankAccount))  # True
print(isinstance(account2, BankAccount))  # True

# Testing deposit and withdrawal
try:
    account1.deposit(2000)
    account1.withdraw(300)
    account1.deposit(-200)  # This will raise a ValueError
except ValueError as e:
    print(e)

try:
    account2.deposit("Not an integer")  # This will raise a ValueError
except ValueError as e:
    print(e)