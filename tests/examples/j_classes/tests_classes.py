import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_bank_account_get_balance(self):
        account1 = BankAccount(500)

        self.assertEqual(account1.get_balance(), 500)

        account2 = BankAccount(600)
        self.assertEqual(account2.get_balance(), 600)