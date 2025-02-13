import unittest

from src.examples.c_decisions.decisions import compare_numbers_equality, get_generation, is_consonant, is_even, is_number_in_range, is_vowel, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):

        self.assertEqual(False and False, False)
        self.assertEqual(True and False, False)
        self.assertEqual(False and True, False)
        self.assertEqual(True and True, True)

    def test_or_truth_table(self):

        self.assertEqual(False or False, False)
        self.assertEqual(True or False, True)
        self.assertEqual(False or True, True)
        self.assertEqual(True or True, True)

    def test_not_truth_table(self):

        self.assertEqual(not False, True)
        self.assertEqual(not True, False)

    def test_compare_numbers_equality(self):
        self.assertEqual(compare_numbers_equality(10, 5), False)
        self.assertEqual(compare_numbers_equality(10, 10), True)

    def test_is_number_in_range(self):
        self.assertEqual(is_number_in_range(1, 10, -1), False)
        self.assertEqual(is_number_in_range(1, 10, 5), True)
        self.assertEqual(is_number_in_range(1, 10, 11), False)

    def test_is_vowel(self):
        self.assertEqual(is_vowel('b'), False)
        self.assertEqual(is_vowel('a'), True)
        self.assertEqual(is_vowel('e'), True)
        self.assertEqual(is_vowel('i'), True)
        self.assertEqual(is_vowel('o'), True)
        self.assertEqual(is_vowel('u'), True)
        self.assertEqual(is_vowel('m'), False)

    def test_is_consonant(self):
        self.assertEqual(is_consonant('a'), False)
        self.assertEqual(is_consonant('b'), True)
        self.assertEqual(is_consonant('c'), True)        
        self.assertEqual(is_consonant('e'), False)

    def test_is_even(self):
        self.assertEqual(is_even(3), False)#not even
        self.assertEqual(is_even(2), True)#even
        self.assertEqual(is_even(5), False)

    def test_get_generation(self):
        self.assertEqual(get_generation(1900), "Invalid Year")
        self.assertEqual(get_generation(1920), "The Greatest Generation")
        self.assertEqual(get_generation(1930), "The Silent Generation")
        self.assertEqual(get_generation(1950), "Baby Boomer Generation")
        self.assertEqual(get_generation(1970),  "Generation X")
        self.assertEqual(get_generation(1985), "Generation Y")
        self.assertEqual(get_generation(2000), "Generation Z")
        self.assertEqual(get_generation(2020), "Generation Alpha")
        self.assertEqual(get_generation(2030),  "Invalid Year")

