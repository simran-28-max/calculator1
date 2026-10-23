import pytest

@pytest.mark.parametrize("number", [10,20,30])
def test_number(number):
    assert number>0
    assert number<0