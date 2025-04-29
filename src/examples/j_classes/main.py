from bank_account import BankAccount
from atm import ATM
from bank_account_db import BankAccountDB

def main():
    
    bankAccountDB = BankAccountDB()
    account1 = BankAccount(bankAccountDB.get_current_balance()) #variable represents a BankAccount--- object or instance of a class
    atm = ATM(account1)

    atm.display_balance()
    atm.make_deposit()
    atm.make_withdraw()

    atm.display_balance()
    print(account1.get_balance())

main()