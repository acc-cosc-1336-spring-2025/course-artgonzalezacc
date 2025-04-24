class BankAccount: #encapsulates variables and functions

    __balance = 0 #variables PRIVATE

    def __init__(self, balance): #constructor - assign values to class private members/variables
        self.__balance = balance

    def get_balance(self): #functions/methods 
        return self.__balance;

    def deposit(self, amount):

        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance -= amount


#FREE FUNCTION(DOESN'T BELONG TO THE BANKACCOUNT CLASS)
def make_deposit(account):
    print(id(account))
    amt = 100
    account.deposit(amt)

def modify_num(num):
    print(id(num)) # research why same address displayed; but different value in test case
    num = 10
