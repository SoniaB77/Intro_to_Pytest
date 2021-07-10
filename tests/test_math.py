import pytest

# basic test case using pytest. Run test in command line using python -m pytest.


@pytest.mark.math
def test_six_plus_seven():
    assert 6 + 7 == 13


# test case with variables.


@pytest.mark.math
def test_eight_plus_nine():
    a = 8
    b = 9
    c = 17
    assert a + b == c


# a test case with an exception.


@pytest.mark.math
def test_divide_by_zero():
    num = 1 / 0


# test catches the exception:


@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


# parameterized test


products = [
    (2, 3, 6),        # positive integers
    (1, 99, 99),      # identity
    (0, 99, 0,),      # zero
    (3, -4, -12),     # positive by negative
    (-5, -5, 25),     # negative by negative
    (2.5, 6.7, 16.75) # floats
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product



