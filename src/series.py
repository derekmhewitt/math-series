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
        raise ValueError("Bad Input.")
    else:
        raise ValueError("Bad Input.")


def lucas(n):
    """Find nth in Lucas sequence."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, f_num=0, s_num=1):
    """Find nth in a series defined by first and second."""
    sum_list = [f_num, s_num]
    if isinstance(n, int) and n > 0:
        for iterations in range(n):
            first = sum_list[len(sum_list) - 2]
            second = sum_list[len(sum_list) - 1]
            sum_list.append(first + second)
        return sum_list[n - 1]
    elif n == 0:
        raise ValueError
    else:
        raise ValueError


if __name__ == '__main__':
    print(u"This module defines 3 functions that implement different mathematical series.")
    print("fibonacci(n)")
    print(u"The first function this module contains outputs the value of the nth Fibonacci number. This is the output of the Fibonacci function called with n = 7:")
    print(u">>> fibonacci(7)")
    print(fibonacci(7))
    print(u"The second function this module contains outputs the value of the nth Lucas number. This is the output of the Lucas function called with n = 5:")
    print(u">>> lucas(5)")
    print(lucas(5))
    print(u"The thrid and final function in this module outputs the value of the nth number in Fibonacci or Lucas -like sequence defined by the user with it's second and third arguments. This is the output of the sum_series function called with n = 3, a = 5 and b = 7:")
    print(u">>> sum_series(3, 5, 7)")
    print(sum_series(3, 5, 7))
    print(u"You can also execute sum_series with just an n argument and it will default to a Fibonacci number output:")
    print(u">>> sum_series(6)")
    print(sum_series(6))
    print(u"This test that shows that our functions raise value errors on bad inputs.")
    print(u">>> fibonacci('taco')")
    print(fibonacci('taco'))
