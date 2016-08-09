# -*- coding: utf-8 -*-
"""series file."""


def fibonacci(n):
    """Find nth value in Fibonacci sequence."""
    fib_list = [0, 1]
    for iterations in range(n):
        first = fib_list[len(fib_list) - 2]
        second = fib_list[len(fib_list) - 1]
        fib_list.append(first + second)
    return fib_list[n - 1]
