class BankAccount:
    account_list=[]

    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance < amount):
            print("insufficient funds: charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (1+self.int_rate)
            return self
        else:
            return self

account1 = BankAccount(.1, 100)
# account1.deposit(100).deposit(50).deposit(75).withdraw(40).yield_interest().display_account_info()

account2 = BankAccount (.2)
account2.deposit(20).deposit(100).withdraw(50).withdraw(80).withdraw(30).withdraw(10).yield_interest().display_account_info()