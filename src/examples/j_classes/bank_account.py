class BankAccount: #encapsulates variables and functions

    __balance = 0 #variables PRIVATE

    def __init__(self, balance): #constructor - assign values to class private members/variables
        self.__balance = balance

    def get_balance(self): #functions/methods 
        return self.__balance;

    def deposit(self, amount):

        if(amount > 0):
            self.__balance += amount