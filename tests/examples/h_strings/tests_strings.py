import unittest

from src.examples.h_strings.strings import string_params, string_return_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_params(self):
        str1 = "Python"
        
        string_params(str1)
        self.assertEqual(str1, "Python")
        
        str1 = "C++"
        self.assertEqual(str1, "C++")

    def test_string_return_value(self):
        lang = "Python"
        print(id(lang))

        lang1 = string_return_value(lang)
        print(id(lang1))

        self.assertEqual(lang, "Python")
        self.assertEqual(lang1, "C++")

