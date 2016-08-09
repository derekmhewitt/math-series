# -*- coding: utf-8 -*-
"""series file."""


def fibonacci(n):
    """Find nth value in Fibonacci sequence."""
    fib_list = [0, 1]
    if isinstance(n, int) and n > 0:
        for iterations in range(n):
            first = fib_list[len(fib_list) - 2]
            second = fib_list[len(fib_list) - 1]
            fib_list.append(first + second)
        return fib_list[n - 1]
    elif n == 0:
        return 0
    else:
        raise ValueError('Please input a positive integer.')


def lucas(n):
    """Find nth in Lucas sequence."""
    if n == 1:
        return 2
    if n == 2:
        return 1
        
