import unittest

from src.examples.j_classes.more_classes.roll import Roll
from src.examples.j_classes.more_classes.die import Die
from src.examples.j_classes.bank_account_db import BankAccountDB
from src.examples.j_classes.bank_account import BankAccount, get_account_object, make_deposit, modify_num

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

    
    def test_get_account_object(self):
        account = get_account_object()
        print("object", id(account))

    def test_bank_account_db_get_current_balance(self):
        db = BankAccountDB();

        self.assertEqual(True, db.get_current_balance() >= 1)
        self.assertEqual(True, db.get_current_balance() <= 10000)

    def test_die_rolls_values_1_to_6(self):
        die = Die()

        for i in range(0, 20):
            rolled_value = die.roll()
            self.assertEqual(rolled_value >= 1, True)
            self.assertEqual(rolled_value <= 6, True)

    def test_roll_for_values_1_to_12(self):
        die1 = Die()
        die2 = Die()

        for i in range(0, 24):
            roll = Roll(die1, die2)
            rolled_value = roll.roll_value()
            self.assertEqual(rolled_value >= 2, True)
            self.assertEqual(rolled_value <= 12, True)

