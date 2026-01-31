from app import add, mul, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(3, 2) == 1

def test_mul():
    assert mul(2, 3) == 6