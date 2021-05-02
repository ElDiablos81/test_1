import unittest
import inspect

def add(x, y):
    print("We're in custom made function : " + inspect.stack()[0][3])
    return(x + y)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        self.assertEqual(add(2, 3), 5)

    def test_case02(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_var = 3.14
        self.assertTrue(isinstance(my_var, float))

    def test_case03(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        self.assertEqual(add(2, 2), 5)

    def test_case04(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        my_var = 3.14
        self.assertTrue(isinstance(my_var, int))


class TestClass04(unittest.TestCase):
    def test_case01(self):
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

class TestClass05(unittest.TestCase):
    def test_case01(self):
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

if __name__ == '__main__':
    unittest.main()
