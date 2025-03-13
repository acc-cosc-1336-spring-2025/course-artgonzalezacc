import unittest

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement, get_reverse_string

class Test_Config(unittest.TestCase):
    
    def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)

    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement('AAAACCCGGT'), 'ACCGGGTTTT')

    def test_get_reverse_strings(self):
        self.assertEqual(get_reverse_string('AAAACCCGGT'), 'TGGCCCAAAA')