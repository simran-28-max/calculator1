import pytest
@pytest.fixture
def employee():
    return{ "name": "Simran",
           "dept": "HR",
           "salary": 40000

    } 

def test_employee(employee):
    assert employee["name"]=="Simran"
def test_employee_dept(employee):
    assert employee["dept"]=="HR"