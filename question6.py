class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance after deposit =", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance after withdraw =", self.balance)

acc = BankAccount("Rishabh", 10000)

acc.deposit(2000)

acc.withdraw(3000)
