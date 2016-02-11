# -*- coding: utf-8 -*-

import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest


class TestMain(unittest.TestCase):

    def test_main(self):
        from prints_a_multiplication_table_of_primes_numbers import PrimeTable
        PrimeTable

    def test_PrimeGenerator(self):
        from prints_a_multiplication_table_of_primes_numbers.prime_generator import PrimeGenerator

        pg = PrimeGenerator()

        self.assertEqual(pg.generate_n_primes(1), [2])
        self.assertEqual(pg.generate_n_primes(2), [2, 3])
        self.assertEqual(pg.generate_n_primes(3), [2, 3, 5])
        self.assertEqual(pg.generate_n_primes(4), [2, 3, 5, 7])
        self.assertEqual(pg.generate_n_primes(5), [2, 3, 5, 7, 11])
        self.assertEqual(pg.generate_n_primes(6), [2, 3, 5, 7, 11, 13])
        self.assertEqual(pg.generate_n_primes(7), [2, 3, 5, 7, 11, 13, 17])
        self.assertEqual(pg.generate_n_primes(8), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(pg.generate_n_primes(9), [2, 3, 5, 7, 11, 13, 17, 19, 23])
        self.assertEqual(pg.generate_n_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    unittest.main()
