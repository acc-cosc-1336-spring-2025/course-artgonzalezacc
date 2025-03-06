import unittest

from src.examples.h_strings.strings import string_params, string_return_value, test_config, validate_password

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

    def test_search_string_w_in(self):
        text = "Four score and seven years ago"

        is_in = 'seven' in text

        self.assertEqual(is_in, True)

    def test_search_string_w_in_2(self):
        text = "Four score and seven years ago"

        is_in = 'Seven' in text

        self.assertEqual(is_in, False)

    def test_search_w_not_in(self):
        text = "Four score and seven years ago"

        not_in = 'Seven' not in text

        self.assertEqual(not_in, True)

    def test_string_isdigit(self):
        str = "123"

        self.assertEqual(str.isdigit(), True)

    def test_string_not_isdigit(self):
        str = "OneTwoThree"

        self.assertEqual(str.isdigit(), False)

    def test_string_isupper(self):
        str = "OneTwoThree"

        self.assertEqual(str.isupper(), False)

    def test_string_lower(self):
        str = "aBCd"

        self.assertEqual(str.lower(), "abcd")

    def test_string_upper(self):
        str = 'abcd'

        self.assertEqual(str.upper(), "ABCD")
        self.assertEqual(str, "abcd")

    def test_string_rstrip(self):
        str = 'abcd '
        expected_str = 'abcd'
        stripped_str = str.rstrip()

        self.assertEqual(expected_str, stripped_str)

    def test_string_find(self):
        text = "Four score and seven years ago"
        index = text.find("score")

        self.assertEqual(index, 5)

    def test_string_not_find(self):
        text = "Four score and seven years ago"
        index = text.find("Score")

        self.assertEqual(index, -1)

    def test_validate_password(self):
        password = 'Leopard6'

        self.assertEqual(validate_password(password), True)

    def test_invalid_password(self):
        password = 'kangaroo'

        self.assertEqual(validate_password(password), False)


    

    

