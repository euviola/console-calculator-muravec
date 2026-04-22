from calculator import add, subtract

def test_add():
    assert add(2,3) == 15

def test_subtract():
    assert subtract(5,3) == 2