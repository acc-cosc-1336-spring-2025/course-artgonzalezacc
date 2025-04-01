import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_dictionary_value(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual(phone_book['Chris'], '555-1111')
        self.assertEqual(phone_book['Katie'], '555-2222')
        self.assertEqual(phone_book['Joanne'], '555-3333')

