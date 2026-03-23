# Fibonacci Iterator

## Description
This project implements a Fibonacci iterable class in Python.

It generates a sequence of Fibonacci numbers up to a given number `n`.

---

## Features
- Uses an iterable class (`__iter__` and `__next__`)
- Handles invalid input (raises `ValueError`)
- Handles negative numbers (returns empty sequence)
- Passes all unit tests using `pytest`

---

## Usage

```python
from fibonacci import Fibonacci

fib = Fibonacci(5)

for num in fib:
    print(num)
