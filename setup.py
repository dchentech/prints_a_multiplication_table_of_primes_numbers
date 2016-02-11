# -*-coding:utf-8-*-

from setuptools import setup


setup(
    name='prints_a_multiplication_table_of_primes_numbers',
    version='0.0.1',
    url='http://github.com/mvj3/prints_a_multiplication_table_of_primes_numbers/',
    license='MIT',
    author='David Chen',
    author_email=''.join(reversed("moc.liamg@emojvm")),
    description='Write a program that prints a multiplication table of primes numbers.',
    long_description=open("README.md").read(),
    packages=['prints_a_multiplication_table_of_primes_numbers'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        "tabulate",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
