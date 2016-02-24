# -*- coding: utf-8 -*-

__all__ = ["FibonacciGenerator"]


class FibonacciGenerator(object):
    """
    """

    # We use List to cache already founded fibonacci numbers,
    # and 1 is the first fibonacci number.
    _fibonacci_list = [0, 1]  # 0 is placeholder
    skip_the_placeholder_idx = 1

    def generate_n_fibonacci_numbers(self, n):
        with_placehoder_len = n + 2
        while len(self._fibonacci_list) < with_placehoder_len:
            self._fibonacci_list.append(self.find_next_fibonacci())

        return self._fibonacci_list[self.skip_the_placeholder_idx:n+1]

    def find_next_fibonacci(self):
        """
        find the next fibonacci after the last number of `self._fibonacci_list`
        """
        assert len(self._fibonacci_list[-2:]) == 2, self._fibonacci_list[-2:]
        last2_num, last1_num = self._fibonacci_list[-2:]
        return last2_num + last1_num
