import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_list_as_parameter(self):
        list1 = [5, 3, 10]
        print('')
        print(id(list1[0]))
        
        
        expected_list = list1
        print(id(expected_list[0]))

        list_as_parameter(list1)

        self.assertEqual(list1[0],100)
        self.assertEqual(list1, expected_list)

