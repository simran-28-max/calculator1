import pytest
@pytest.mark.parametrize("username", ["Simran", "Ekam", "Karan"])
def test_username(username):
    assert username!=""
    assert username=""