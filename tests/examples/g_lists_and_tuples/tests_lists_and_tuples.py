import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter, list_as_return_value

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

    def test_list_as_return_value(self):
        list1  =[5, 3, 10]
        print('')
        print('test list1' + str(id(list1[0])))

        expected_list = list1
        print('test expected ' + str(id(expected_list[0])))

        returned_list = list_as_return_value(list1)
        print('test return list ' + str(id(returned_list[0])))
        
        self.assertEqual(list1[0], returned_list[0])
