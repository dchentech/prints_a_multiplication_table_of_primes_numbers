# -*- coding: utf-8 -*-

__all__ = ["PrimeGenerator", "NumLines"]

from .prime_generator import PrimeGenerator
from .num_lines import NumLines
from .tabulate_ext import tabulate_prime


class PrimeTable(object):
    """
    Generate a multiplication table of primes numbers.
    """
    pg = PrimeGenerator()

    @classmethod
    def output(cls, number):
        primes_numbers = cls.pg.generate_n_primes(number)
        lines = NumLines.generate(primes_numbers)

        # tabulate's output don't meet the prime table format requirement, and the
        # `tabulate` module has some hard code, so we modify the output string directly.
        output = tabulate_prime(lines)

        return output
