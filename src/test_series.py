# -*- coding: utf-8 -*-
"""test_series file."""


def test_fibonacci_1():
    """Test_fib_1 with value 0."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_2():
    """Test_fib_2 with value 8."""
    from series import fibonacci
    assert fibonacci(7) == 8
