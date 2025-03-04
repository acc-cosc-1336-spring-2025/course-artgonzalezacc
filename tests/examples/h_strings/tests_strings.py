import unittest

from src.examples.h_strings.strings import string_params, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_params(self):
        str1 = "Python"
        
        string_params(str1)
        self.assertEqual(str1, "Python")
        
        str1 = "C++"
        self.assertEqual(str1, "C++")

