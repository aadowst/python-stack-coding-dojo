class BankAccount:
    account_list=[]

    def __init__(self, account_type, int_rate, balance=0): 
        self.account_type = account_type
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_list.append(self)

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

    @classmethod
    def all_balances(cls):
        for entry in cls.account_list:
            print(entry.account_type, entry.balance)

class User:
    user_list = []
    def __init__(self, name, email, account_type, int_rate, balance):
        self.name = name
        self.email = email
        self.account = {account_type: BankAccount(account_type, int_rate, balance)}
        User.user_list.append(self)

    def add_account(self, account_type, int_rate, balance):
        self.account[account_type] = BankAccount(account_type, int_rate, balance)

    def make_deposit(self, account_type, amount):

        self.account[account_type].deposit(amount)
        return self

    # def make_withdrawal(self, account_number, amount):
    #     if (account_number == "account1"):
    #         self.account1.withdraw(amount)
    #         return self
    #     elif (account_number == "account2"):
    #         self.account1.withdraw(amount)
    #         return self
    #     else:
    #         return self
    
    def display_user_balance(self, account_type):
        print(self.account[account_type].balance)
        return self

    @classmethod
    def print_balances(cls):
        for entry in cls.user_list:
            print(entry.name, entry.account)


User1 = User("Mr. Smartypants", "smarty@pants.com", "checking", 0.1, 1000)
# print(User1.name)
User1.add_account("savings", 0.1, 2000)

User1.display_user_balance("checking")
User1.display_user_balance("savings")

# User1.make_deposit("account1", 500)

# print(User1.account.balance)
# User1.account.deposit(2000)
# print(User1.account.balance)
# User1.make_deposit(1000)
# print(User1.display_user_balance())

# BankAccount.all_balances()
# User.print_balances()
