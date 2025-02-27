import unittest

from src.examples.e_functions.value_return_functions import get_random_number, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_random_number(self):
        self.assertEqual(get_random_number(1, 100) >= 1, True)
        self.assertEqual(get_random_number(1, 100) <= 100, True)

