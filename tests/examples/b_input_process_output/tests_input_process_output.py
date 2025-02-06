import unittest

from src.examples.b_input_proc_output.input_process_output import add_numbers, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 15), 25)
        self.assertEqual(add_numbers(50, 15), 65)

