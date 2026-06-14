class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):            
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} ")

    def withdraw(self, amount):
        if amount > self.balance:
              return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount} ")
        return f"Newbalance: {self.balance} "
    
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance} "
    
class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Applied interest: {interest: .2f} ")
        return f"New balance after interest: {self.balance:.2f} "

owner1 = SavingAccount("cyril", 1000)
print(owner1)
print(owner1.deposit(500))
print(owner1.withdraw(200))
print(owner1.withdraw(2000))
print(owner1.transaction_history)
print(owner1.apply_interest())  # This will raise an AttributeError since apply_interest is not defined in BankAccount
print("===============================================")