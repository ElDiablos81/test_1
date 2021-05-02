def mul(a, b):
    """
    :param a:2
    :param b:3
    :return:6
    """
    return a * b

def add(a, b):
    """
>>> add(2, 3)
5

>>> add('a', 'b')
'ab'
    """
    return a + b

def test_mul_true():
    assert mul(2,3) == 6

def test_mul_false():
    assert mul(2,2) == 5

def test_add_true():
    assert add('a', 'b') == 'ab'