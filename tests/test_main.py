# -*- coding: utf-8 -*-

import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest
from prints_a_multiplication_table_of_primes_numbers import PrimeTable


class TestMain(unittest.TestCase):

    def test_main(self):
        PrimeTable


if __name__ == '__main__':
    unittest.main()
