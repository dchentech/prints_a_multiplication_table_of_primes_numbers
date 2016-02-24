# -*- coding: utf-8 -*-

import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest


class TestMain(unittest.TestCase):

    def test_main(self):
        # NOTE the blank index of result is a minor different to the requirement.
        # If the requirement is confirmed to be very strict, then feel free to contact me,
        # and I'll write a manual one.
        from prints_a_multiplication_table_of_primes_numbers import PrimeTable

        count_1_output = """
   |  2
---+---
 2 |  4""".lstrip("\n")
        self.assertEqual(PrimeTable.output(1), count_1_output)

        count_10_output = """
   |  2   3   5   7   11   13   17   19   23   29
---+---------------------------------------------
 2 |  4   6  10  14   22   26   34   38   46   58
 3 |  6   9  15  21   33   39   51   57   69   87
 5 | 10  15  25  35   55   65   85   95  115  145
 7 | 14  21  35  49   77   91  119  133  161  203
11 | 22  33  55  77  121  143  187  209  253  319
13 | 26  39  65  91  143  169  221  247  299  377
17 | 34  51  85 119  187  221  289  323  391  493
19 | 38  57  95 133  209  247  323  361  437  551
23 | 46  69 115 161  253  299  391  437  529  667
29 | 58  87 145 203  319  377  493  551  667  841""".lstrip("\n")
        self.assertEqual(PrimeTable.output(10), count_10_output)

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

    def test_FibonacciGenerator(self):
        from prints_a_multiplication_table_of_primes_numbers.fibonacci_generator import FibonacciGenerator

        fg = FibonacciGenerator()

        self.assertEqual(fg.generate_n_fibonacci_numbers(1), [1])
        self.assertEqual(fg.generate_n_fibonacci_numbers(2), [1, 1])
        self.assertEqual(fg.generate_n_fibonacci_numbers(3), [1, 1, 2])
        self.assertEqual(fg.generate_n_fibonacci_numbers(4), [1, 1, 2, 3])
        self.assertEqual(fg.generate_n_fibonacci_numbers(5), [1, 1, 2, 3, 5])
        self.assertEqual(fg.generate_n_fibonacci_numbers(6), [1, 1, 2, 3, 5, 8])

    def test_NumLines(self):
        from prints_a_multiplication_table_of_primes_numbers.num_lines import NumLines

        self.assertEqual(NumLines.generate([2, 3, 5, 7, 11]), [
            ["", 2, 3, 5, 7, 11],
            [2, 4, 6, 10, 14, 22],
            [3, 6, 9, 15, 21, 33],
            [5, 10, 15, 25, 35, 55],
            [7, 14, 21, 35, 49, 77],
            [11, 22, 33, 55, 77, 121]])

        self.assertEqual(NumLines.generate([2]), [
            ["", 2],
            [2, 4], ])


if __name__ == '__main__':
    unittest.main()
