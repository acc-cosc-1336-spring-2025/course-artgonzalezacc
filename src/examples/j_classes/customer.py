class Customer:
    def __init__(self, account):
        self.__account = account;

    def get_bank_account(self):
        return self.__account