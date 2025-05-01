from bank_account import BankAccount
from bank_account_db import BankAccountDB
from customer import Customer
from random import randint

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

#free functions - not part of the atm class
db = BankAccountDB()
customers = []
customers.append(Customer(BankAccount(0), BankAccount(db.get_current_balance())))
customers.append(Customer(BankAccount(0), BankAccount(db.get_current_balance())))
customers.append(Customer(BankAccount(0), BankAccount(db.get_current_balance())))


def display_menu():
    print('ACC Example Bank')
    print('1-Display Balance')
    print('2-Make Deposit')
    print('3-Make Withdraw')
    print('4-Exit')

def run_menu():
    choice = 0

    
    while(True):
        num = input("press enter to start: ")
        customer_index = randint(0, len(customers)-1)
        customer = customers[customer_index]

        account_index = int(input("Enter 1 for Checking 2 for Savings: "))
        account = customer.get_bank_account(account_index-1)
        atm = ATM(account)

        while(choice != 4):
            display_menu()
            choice = int(input("Enter menu choice: "))

            handle_user_choice(atm, choice)

        if(choice == 4):
                choice = 0

def handle_user_choice(atm, choice):
    if(choice == 1):
        atm.display_balance()
    elif(choice == 2):
        atm.make_deposit()
    elif(choice == 3):
        atm.make_withdraw()
    elif(choice == 4):
        print('Exiting...')
    else:
        print("Invalid choice.")