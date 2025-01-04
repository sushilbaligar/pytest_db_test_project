
import pytest

pytestmark = [pytest.mark.fast,pytest.mark.slow]

@pytest.fixture(scope="module")
def my_setup():
    print("\n>>>> My SETUP <<<<<<")
    return {'id':20,'name':'sush'}

@pytest.mark.smoke
@pytest.mark.ll
def test_first(my_setup):
    print("first_test executed")
    print(my_setup)
    print(my_setup.get('id'))
    print(my_setup.get('name'))

def test_second():
    print("second test executed")
    #assert 1==2, print("one is not two")

def test_third():
    print("third test executed")