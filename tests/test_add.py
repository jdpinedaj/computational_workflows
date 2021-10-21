import numpy as np
from add import add
import pytest

def test_adding():
    c = add(30, 20)
    assert(c == 50)

def test_adding_float():
    c = add(50.0, 30.0)
    assert(np.isclose(c, 80.0))

@pytest.mark.parametrize("a, b, result", [(3, 5, 8), (-3, 4, 1), (10, -3, 7)])
def test_add_param(a, b, result):
    c = add(a, b)
    assert(c == result)
