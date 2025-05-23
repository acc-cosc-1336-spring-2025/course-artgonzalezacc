import random

class BankAccount: #encapsulates variables and functions

    __balance = 0 #variables PRIVATE

    def __init__(self, balance): #constructor - assign values to class private members/variables
        
        if(balance == 0):
            self.__get_balance_from_db()
        else:
            self.__balance = balance

    def get_balance(self): #functions/methods 
        return self.__balance;

    def deposit(self, amount):

        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance -= amount

    def __get_balance_from_db(self):
        self.__balance = random.randint(1, 10000)


#FREE FUNCTION(DOESN'T BELONG TO THE BANKACCOUNT CLASS)
def make_deposit(account):
    print(id(account))
    amt = 100
    account.deposit(amt)

def modify_num(num):
    print(id(num)) # research why same address displayed; but different value in test case
    num = 10

def get_account_object():
    account = BankAccount(50)
    print("get_account_object", id(account))
    return account
