import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_dictionary_value(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual(phone_book['Chris'], '555-1111')
        self.assertEqual(phone_book['Katie'], '555-2222')
        self.assertEqual(phone_book['Joanne'], '555-3333')
        

    def test_invalid_key_access_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        with self.assertRaises(KeyError):
             phone_book['Sam']

    def test_key_in_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual('Katie' in phone_book, True)
        self.assertEqual('Sam' in phone_book, False)

    def test_key_not_in_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        
        self.assertEqual('Sam' not in phone_book, True)
        self.assertEqual('Katie' not in phone_book, False)

    def test_add_key_value_pair_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        if 'Sam' not in phone_book:
            phone_book['Sam'] = '555-4444'

        self.assertEqual(phone_book['Sam'], '555-4444')

    def test_update_value_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        if 'Katie' in phone_book:
            phone_book['Katie'] = '555-1212'

        self.assertEqual(phone_book['Katie'], '555-1212')

    def test_delete_key_value_pair_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        if 'Chris' in phone_book:
            del phone_book['Chris']

        self.assertEqual('Chris' not in phone_book, True)

    def test_get_number_of_elements_dictionary(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual(len(phone_book), 3)

    def test_dictionary_supports_different_data_value_types(self):
        phone_book = {'Chris':5551111, 'Katie':'555-2222', 'Joanne':[555,3333]}

        self.assertEqual(phone_book['Chris'], 5551111)
        self.assertEqual(phone_book['Katie'], '555-2222')
        self.assertEqual(phone_book['Joanne'], [555,3333])

    def test_dictionary_supports_data_key_types(self):
        phone_book = {5551111:'Cris', 'Katie':'555-2222', 50.5:'Joanne'}

        self.assertEqual(phone_book[5551111], 'Cris')
        self.assertEqual(phone_book['Katie'], '555-2222')
        self.assertEqual(phone_book[50.5], 'Joanne')

    def test_dictionary_records(self):
        employee = {'name':'Kevin Smith', 'id':12345, 'payrate':25.75}

        self.assertEqual(employee['name'], 'Kevin Smith')
        self.assertEqual(employee['id'] ,12345)
        self.assertEqual(employee['payrate'], 25.75)

    def test_insert_into_empty_dictionary(self):
        #phone_book = {}
        phone_book = dict()
        phone_book['Chris'] = '555-1111'
        phone_book['Katie'] = '555-2222'
        phone_book['Joanne'] = '555-3333'

        self.assertEqual(phone_book['Chris'], '555-1111')
        self.assertEqual(phone_book['Katie'], '555-2222')
        self.assertEqual(phone_book['Joanne'], '555-3333')

    def test_dictionary_clear(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        phone_book.clear()
        self.assertEqual(phone_book, {})

    def test_dictionary_get(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        result = phone_book.get('Katie', 'Key not found')
        self.assertEqual(result, '555-2222')

        result = phone_book.get('Katy', "Key not found")
        self.assertEqual(result, 'Key not found')

    def test_dictionary_items(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        list_tuple_items = list(phone_book.items()) #[('key', 'value'), ('key2', 'value2') ]
        
        self.assertEqual(list_tuple_items[0], ('Chris', '555-1111'))
        self.assertEqual(list_tuple_items[1], ('Katie', '555-2222'))
        self.assertEqual(list_tuple_items[2], ('Joanne', '555-3333'))

    def test_dictionary_pop_item(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        key, value = phone_book.popitem()

        self.assertEqual(key, 'Joanne')
        self.assertEqual(value, '555-3333')
        self.assertEqual(phone_book, {'Chris':'555-1111', 'Katie':'555-2222'})

    def test_dictionary_values(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        list_values = list(phone_book.values())

        self.assertEqual(list_values[0], '555-1111')
        self.assertEqual(list_values[1], '555-2222')
        self.assertEqual(list_values[2], '555-3333')

    def test_dictionary_keys(self):
        phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        list_keys = list(phone_book.keys())

        self.assertEqual(list_keys[0], 'Chris')
        self.assertEqual(list_keys[1], 'Katie')
        self.assertEqual(list_keys[2], 'Joanne')

    def test_set_union(self):
        set1 = set([1,2,3,4])        
        set2 = set([3,4,5,6])
        expected_set = set([1,2,3,4,5,6])
        union_set = set1.union(set2)

        self.assertEqual(union_set, expected_set)

    def test_set_intersection(self):
        set1 = set([1,2,3,4])        
        set2 = set([3,4,5,6])
        expected_set = set([3,4])
        intersection_set = set1.intersection(set2)

        self.assertEqual(intersection_set, expected_set)

    def test_set_difference(self):
        set1 = set([1,2,3,4])        
        set2 = set([3,4,5,6])
        expected_set = set([1,2])
        difference_set = set1.difference(set2)

        self.assertEqual(difference_set, expected_set)

    def test_set_symmetric_difference(self):
        set1 = set([1,2,3,4])        
        set2 = set([3,4,5,6])
        expected_set = set([1,2,5,6])
        sym_difference_set = set1.symmetric_difference(set2)

        self.assertEqual(sym_difference_set, expected_set)




    





