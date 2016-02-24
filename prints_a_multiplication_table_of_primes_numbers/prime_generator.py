# -*- coding: utf-8 -*-

__all__ = ["PrimeGenerator"]


class PrimeGenerator(object):
    """
    A cache-version of prime list generator.
    """

    # We use List to cache already founded primes,
    # and 2 is the first prime number.
    _primes_list = [2]

    def generate(self, n):
        """ n is the number that how many primes you want to generate. """
        while len(self._primes_list) < n:
            self._primes_list.append(self.find_next_prime())

        return self._primes_list[0:n]

    def find_next_prime(self):
        """
        find the next prime after the last number of `self._primes_list`
        """
        last_num = self._primes_list[-1]
        last_num += 1

        while True:
            is_prime = True
            for _num in self._primes_list:
                if (last_num % _num) == 0:
                    is_prime = False
                    break

            if is_prime:
                break
            else:
                last_num += 1

        return last_num
