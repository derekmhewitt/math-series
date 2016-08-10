# -*- coding: utf-8 -*-
"""test_series file."""
import pytest

FIBONACCI_TABLE = [
    (0, None),
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
    (0, None),
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (10, 76),
    (11, 123)
]

SUM_SERIES_TABLE = [
    (5, 7, 4, 26),
    (4, 3, 4, 11),
    (0, 12, 14, None),
    (-5, 3, 4, None)
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


def test_fibonacci_not_int():
    """Test for not integer inputs."""
    from series import fibonacci
    assert fibonacci('taco') is None


def test_fibonacci_negatives():
    """Test for rejecting negative inputs."""
    from series import fibonacci
    assert fibonacci(-1) is None


def test_lucas_1():
    """Test lucas function with input 1."""
    from series import lucas
    assert lucas(1) == 2


def test_lucas_2():
    """Test lucas function with input 2."""
    from series import lucas
    assert lucas(2) == 1


def test_lucas_7():
    """Test lucas with input 7."""
    from series import lucas
    assert lucas(7) == 18


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas_params(n, result):
    """Test lucas function using the LUCAS_TABLE."""
    from series import lucas
    assert lucas(n) == result


def test_sum_series():
    """Test sum_series function with n = 6 and first = 1, second = 3."""
    from series import sum_series
    assert sum_series(6, 1, 3) == 18


@pytest.mark.parametrize('n, a, b, result', SUM_SERIES_TABLE)
def test_sum_param(n, a, b, result):
    """Test sum_series function against SUM_SERIES_TABLE."""
    from series import sum_series
    assert sum_series(n, a, b) == result
