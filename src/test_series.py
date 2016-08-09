# -*- coding: utf-8 -*-
"""test_series file."""
import pytest

FIBONACCI_TABLE = [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (15, 377),
    (29, 317811)
]

LUCAS_TABLE = [
    (0, 0),
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (10, 76),
    (11, 123)
]


def test_fibonacci_1():
    """Test_fib_1 with value 0."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_2():
    """Test_fib_2 with value 8."""
    from series import fibonacci
    assert fibonacci(7) == 8


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci_param(n, result):
    """Test_fibonacci with params."""
    from series import fibonacci
    assert fibonacci(n) == result


# def test_fibonacci_not_int():
#     """Test for not integer inputs."""
#     from series import fibonacci
#     assert fibonacci('taco') == ValueError


# def test_fibonacci_negatives():
#     """Test for rejecting negative inputs."""
#     from series import fibonacci
#     assert fibonacci(-1) == u'ValueError: Please input a positive integer.'


def test_lucas_1():
    """Test lucas function with input 1."""
    from series import lucas
    assert lucas(1) == 2


def test_lucas_2():
    """Test lucas function with input 2."""
    from series import lucas
    assert lucas(2) == 1
