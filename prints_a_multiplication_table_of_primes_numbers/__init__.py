# -*- coding: utf-8 -*-

__all__ = ["PrimeGenerator", "NumLines"]

from .prime_generator import PrimeGenerator
from .num_lines import NumLines
from .tabulate_ext import tabulate


class PrimeTable(object):
    """
    Generate a multiplication table of primes numbers.
    """
    pg = PrimeGenerator()

    @classmethod
    def output(cls, number):
        primes_numbers = cls.pg.generate_n_primes(number)
        lines = NumLines.generate(primes_numbers)
        output = tabulate(lines, tablefmt="prime", headers="firstrow")
        print output
        return output
