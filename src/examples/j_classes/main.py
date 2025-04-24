from bank_account import BankAccount

def main():
    account1 = BankAccount(500) #variable represents a BankAccount--- object or instance of a class
    print(account1.get_balance())

    amount = input("Enter amount to deposit: ")
    account1.deposit(int(amount))
    print(account1.get_balance())

main()