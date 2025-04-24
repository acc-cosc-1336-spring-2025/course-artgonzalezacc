import unittest

from src.examples.j_classes.bank_account import BankAccount

class Test_Config(unittest.TestCase):

    def test_bank_account_get_balance(self):
        account = BankAccount(500)

        self.assertEqual(account.get_balance(), 500)