from bank_account import BankAccount
from atm import ATM, run_menu
from bank_account_db import BankAccountDB
from customer import Customer

def main():
    
    bankAccountDB = BankAccountDB()
    account1 = BankAccount(bankAccountDB.get_current_balance()) #variable represents a BankAccount--- object or instance of a class
    customer = Customer(account1)
    atm = ATM(customer)

    run_menu(atm)

    print(account1.get_balance())

main()