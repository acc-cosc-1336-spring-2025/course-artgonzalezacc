from bank_account import BankAccount

def main():
    account1 = BankAccount(500) #variable represents a BankAccount--- object or instance of a class
    print(account1.get_balance())

    account2 = BankAccount(600)
    print(account2.get_balance())

main()