def mul(a, b):
    return a * b

def test_mul_true():
    assert mul(2,2) == 4

def test_mul_false():
    assert mul(2,2) == 5