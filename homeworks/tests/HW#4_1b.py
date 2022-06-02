import pytest
from functions_to_test import *

objCalculator = Calculator()


def test_add():
    assert objCalculator.add(5, 7) == 12


def test_subtract():
    assert objCalculator.subtract(5, 2) == 3


def test_multiply():
    assert objCalculator.multiply(2, 3) == 6


def test_divide():
    assert objCalculator.divide(4, 2) == 2
    with pytest.raises(ValueError):
        objCalculator.divide(4, 0)
