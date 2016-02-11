# -*- coding: utf-8 -*-

__all__ = ["PrimeGenerator", "NumLines"]

from .prime_generator import PrimeGenerator
from .num_lines import NumLines
from .tabulate_ext import tabulate


class PrimeTable(object):
    """
    Generate a multiplication table of primes numbers.
    """

    @staticmethod
    def output(number):
        primes_numbers = PrimeGenerator.generate_n_primes(number)
        lines = NumLines.generate(primes_numbers)
        output = tabulate(lines, tablefmt="prime", headers="firstrow")
        return output
