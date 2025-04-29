
class ATM:

    def __init__(self, account):
        self.__account = account

    def display_balance(self):
        print(self.__account.get_balance())

    def make_deposit(self):
        amt = int(input("Enter amount to deposit: "))
        self.__account.deposit(amt)

    def make_withdraw(self):
        amt = int(input("Enter amount to withdraw: "))
        self.__account.withdraw(amt)