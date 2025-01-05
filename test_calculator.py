import pytest
from calculator import square


def square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
    