import unittest

from src.examples.d_repetition.repetition import get_sum_of_squares, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_sum_of_squares(self):
        self.assertEqual(get_sum_of_squares(3), 14)
        self.assertEqual(get_sum_of_squares(4), 30)
        self.assertEqual(get_sum_of_squares(5), 55)

