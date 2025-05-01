class Customer:
    def __init__(self, checking, savings):
        self.__list_accounts = []
        self.__list_accounts.append(checking)
        self.__list_accounts.append(savings)

    def get_bank_account(self, index):
        return self.__list_accounts[index]