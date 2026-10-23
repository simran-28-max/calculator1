import pytest

from calculator import add

@pytest.mark.parametrize("a, b, expected",[
                         (2,3,5),
                         (4,8,12),
                         (1,8,9)])

def test_add(a,b,expected):
    assert add(a,b) == expected



@pytest.fixture
def numbers():
    return(10,20)

def test_add(numbers):
    a,b=numbers
    assert add(a,b)==30    
