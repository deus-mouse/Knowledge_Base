'''
https://www.youtube.com/watch?v=1HtEPEn4-LY
'''


# from ..utils import division
import pytest


def division(a, b):
    return a / b

@pytest.mark.parametrize('a, b, expected_result',
                         [(10, 2, 5),
                         (20, 10, 2),
                         (30, -3, -10),
                          (5, 2, 2.5)
                          ])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_exception, divider, divisionable',
                         [(ZeroDivisionError, 0, 10),
                         (TypeError, "10", 2)
                          ])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)