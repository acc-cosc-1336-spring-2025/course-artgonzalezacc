import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_bank_account_get_balance(self):
        account1 = BankAccount(500)

        self.assertEqual(account1.get_balance(), 500)

        account2 = BankAccount(600)
        self.assertEqual(account2.get_balance(), 600)

    def test_bank_account_deposit(self):
        account1 = BankAccount(500)

        self.assertEqual(account1.get_balance(), 500)

        account1.deposit(100)
        self.assertEqual(account1.get_balance(), 600)

    def test_bank_account_deposit_less_than_0(self):
        account1 = BankAccount(500)
        self.assertEqual(account1.get_balance(), 500)

        account1.deposit(-100)
        self.assertEqual(account1.get_balance(), 500)

    def test_bank_account_withdraw(self):
        account1 = BankAccount(500)
        self.assertEqual(account1.get_balance(), 500)

        account1.withdraw(100)
        self.assertEqual(account1.get_balance(), 400)

    def test_bank_account_withdraw_less_than_0(self):
        account1 = BankAccount(500)
        self.assertEqual(account1.get_balance(), 500)

        account1.withdraw(-100)
        self.assertEqual(account1.get_balance(), 500)

    def test_bank_account_deposit_withdraw(self):
        account1 = BankAccount(500)
        self.assertEqual(account1.get_balance(), 500)

        account1.deposit(100)
        self.assertEqual(account1.get_balance(), 600)

        account1.withdraw(60)
        self.assertEqual(account1.get_balance(), 540)

    def test_bank_account_withdraw_deposit(self):
        account1 = BankAccount(500)
        self.assertEqual(account1.get_balance(), 500)

        account1.withdraw(100)
        self.assertEqual(account1.get_balance(), 400)

        account1.deposit(50)
        self.assertEqual(account1.get_balance(), 450)
