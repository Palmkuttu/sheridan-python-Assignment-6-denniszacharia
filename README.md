Fibonacci Iterator
This project implements a Fibonacci iterable class in Python.

Description
The Fibonacci class generates a sequence of Fibonacci numbers up to a given index n.

It follows the iterator protocol by implementing:

__iter__()
__next__()
Usage
from fibonacci import Fibonacci

fib = Fibonacci(5)
print(list(fib))
