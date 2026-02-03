import pytest
from calculator.add import add
from calculator.subtract import subtract
from calculator.multiply import multiply
from calculator.divide import divide




def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
