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





