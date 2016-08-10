# -*- coding: utf-8 -*-
"""test_series file."""
import pytest

FIBONACCI_TABLE = [
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
    (4, 3, 4, 11)
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
    with pytest.raises(ValueError):
        fibonacci('taco')


def test_fibonacci_negatives():
    """Test for rejecting negative inputs."""
    from series import fibonacci
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_zero():
    """Test for rejecting 0 input."""
    from series import fibonacci
    with pytest.raises(ValueError):
        fibonacci(0)


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


def test_lucas_taco():
    """Test lucas with taco input."""
    from series import lucas
    with pytest.raises(ValueError):
        lucas('taco')


def test_lucas_negative():
    """Test lucas with negative input."""
    from series import lucas
    with pytest.raises(ValueError):
        lucas(-5)


def test_lucas_zero():
    """Test lucas with zero input."""
    from series import lucas
    with pytest.raises(ValueError):
        lucas(0)


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


def test_sum_series_0():
    """Test sum_series with 0 input."""
    from series import sum_series
    with pytest.raises(ValueError):
        sum_series(0, 12, 14)


def test_sume_series_negative():
    """Test sum_series with negative."""
    from series import sum_series
    with pytest.raises(ValueError):
        sum_series(-5, 3, 4)


def test_sum_series_taco():
    """Test sum_series with a taco."""
    from series import sum_series
    with pytest.raises(ValueError):
        sum_series('taco')
