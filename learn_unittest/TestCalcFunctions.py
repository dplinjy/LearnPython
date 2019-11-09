import unittest
import random
from Calc import Calc

class TestCalcFunctions(unittest.TestCase):

    def setUp(self):
        self.c = Calc()
        print("setup completed")

    def test_sum(self):
        print("run sum()")
        self.assertTrue(self.c.add(1, 2, 3, 4) == 10)

    def test_sub(self):
        print("run sub()")
        self.assertTrue(self.c.sub(100, 20, 30, 40) == 10)

    def test_mul(self):
        print("run mul()")
        self.assertTrue(self.c.mul(1, 2, 3, 40) == 240)

    def test_div(self):
        print("run div()")
        self.assertTrue(self.c.div(100, 10, 2) == 5)

    def tearDown(self):
        print("test completed")

    def tearDOwn(self):
        print("tearDown completed")


if __name__ == '__main__':
    unittest.main()