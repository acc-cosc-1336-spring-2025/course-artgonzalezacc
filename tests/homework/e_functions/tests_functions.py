import unittest

from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds

class Test_Config(unittest.TestCase):
    def test_get_hour(self):
        self.assertEqual(get_hour(3800), 1)
        self.assertEqual(get_hour(1741832545), 2)

    def test_get_minutes(self):
        self.assertEqual(get_minutes(3800), 3)
        self.assertEqual(get_minutes(1741832545), 22)

    def test_get_seconds(self):
        self.assertEqual(get_seconds(3800), 20)
        self.assertEqual(get_seconds(1741832545), 25)

