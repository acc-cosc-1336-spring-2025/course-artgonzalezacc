from bank_account import BankAccount
from atm import ATM, run_menu
from bank_account_db import BankAccountDB

def main():
    
    bankAccountDB = BankAccountDB()
    account1 = BankAccount(bankAccountDB.get_current_balance()) #variable represents a BankAccount--- object or instance of a class
    atm = ATM(account1)

    run_menu(atm)

    print(account1.get_balance())

main()