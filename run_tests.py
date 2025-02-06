import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
from tests.examples.b_input_process_output import tests_input_process_output

suite = unittest.TestLoader().loadTestsFromModule(tests_input_process_output)
unittest.TextTestRunner(verbosity=2).run(suite)
