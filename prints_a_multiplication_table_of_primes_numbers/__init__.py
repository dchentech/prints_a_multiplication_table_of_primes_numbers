# -*- coding: utf-8 -*-

__all__ = ["PrimeTable"]

from .prime_generator import PrimeGenerator
from .fibonacci_generator import FibonacciGenerator
from .num_lines import NumLines
from .tabulate_ext import tabulate_prime


class PrimeTable(object):
    """
    Generate a multiplication table of primes numbers.
    """
    pg = PrimeGenerator()
    fg = FibonacciGenerator()
    algorithms = {
        "prime": pg,
        "fibonacci": fg,
    }

    @classmethod
    def output(cls, number, algorithm="prime"):
        exe = cls.algorithms.get(algorithm, None)
        numbers = exe.generate(number)
        lines = NumLines.generate(numbers)

        # tabulate's output don't meet the prime table format requirement,
        # and the `tabulate` module has some hard code, so we modify the
        # output string directly.
        output = tabulate_prime(lines)

        return output
