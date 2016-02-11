# Coding challenge - prints a multiplication table of primes numbers
[![Build Status](https://img.shields.io/travis/mvj3/prints_a_multiplication_table_of_primes_numbers/master.svg?style=flat)](https://travis-ci.org/mvj3/prints_a_multiplication_table_of_primes_numbers)

### Objective

Write a program that prints a multiplication table of primes numbers. The program should take an argument from the command line that specifies the amount of prime numbers to generate and print out a multiplication table for these prime numbers.

An example of the way the application may run:

```bash
<executable_script_name> --count 10
```

An example of the output:

```text
   |  2   3   5   7  11  13  17  19  23  29
---+---------------------------------------
 2 |  4   6  10  14  22  26  34  38  46  58
 3 |  6   9  15  21  33  39  51  57  69  87
 5 | 10  15  25  35  55  65  85  95 115 145
 7 | 14  21  35  49  77  91 119 133 161 203
11 | 22  33  55  77 121 143 187 209 253 319
13 | 26  39  65  91 143 169 221 247 299 377
17 | 34  51  85 119 187 221 289 323 391 493
19 | 38  57  95 133 209 247 323 361 437 551
23 | 46  69 115 161 253 299 391 437 529 667
29 | 58  87 145 203 319 377 493 551 667 841
```


Please provide a compressed file with your application source and, when applicable, any source control files.

### Notes

1. Consider code readability/complexity
2. Consider SOLID / functional principles, but do not over-engineer
3. Consider extensibility
4. Feel free to use any library, except in the case of prime number generation
5. Consider how you can prove the correctness of your application
6. You can write it in Ruby, Clojure, Python or Perl.
