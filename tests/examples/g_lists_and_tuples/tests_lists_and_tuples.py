import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter, list_as_return_value, list_as_return_value_no_param, get_total_value_of_list_items_while, get_total_value_of_list_items_for_range, get_total_value_of_list_items_for, get_multiplication_table
    

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

    def test_list_as_return_value_no_param(self):

        return_list = list_as_return_value_no_param()
        print('test return list ' + str(id(return_list[0])))

        self.assertEqual(True, True)

    def test_get_total_value_of_list_items_while(self):

        self.assertEqual(get_total_value_of_list_items_while(), 30)

    def test_get_total_value_of_list_items_for_range(self):

        self.assertEqual(get_total_value_of_list_items_for_range(), 30)

    def test_get_total_value_of_list_items_for(self):

        self.assertEqual(get_total_value_of_list_items_for(), 30)

    def test_two_dimensional_list_indexing(self):
        sub_list1 = [20, 5, 10]
        sub_list2 = [100, 150, 75]
        sub_list3 = [7, 10, 15]

        two_d_list = [sub_list1, sub_list2, sub_list3]

        self.assertEqual(two_d_list[0][0], 20)
        self.assertEqual(two_d_list[0][1], 5)
        self.assertEqual(two_d_list[0][2], 10)
        self.assertEqual(two_d_list[1][0], 100)
        self.assertEqual(two_d_list[1][1], 150)
        self.assertEqual(two_d_list[1][2], 75)
        self.assertEqual(two_d_list[2][0], 7)
        self.assertEqual(two_d_list[2][1], 10)
        self.assertEqual(two_d_list[2][2], 15)

    def test_two_dimensional_list_row_indexing(self):
        sub_list1 = [20, 5, 10]
        sub_list2 = [100, 150, 75]
        sub_list3 = [7, 10, 15]

        two_d_list = [sub_list1, sub_list2, sub_list3]

        self.assertEqual(two_d_list[0], sub_list1)
        self.assertEqual(two_d_list[1], sub_list2)
        self.assertEqual(two_d_list[2], sub_list3)

    def test_multiplication_table_3x3(self):
        expected_ones_row = [1, 2, 3]
        expected_twos_row = [2, 4, 6]
        expected_threes_row =[3, 6, 9]

        multi_table = get_multiplication_table(3, 3)

        self.assertEqual(multi_table[0], expected_ones_row)
        self.assertEqual(multi_table[1], expected_twos_row)
        self.assertEqual(multi_table[2], expected_threes_row)
