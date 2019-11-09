import unittest
from Calc import Calc


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("单元测试前，创建Calc类实例")
        cls.c = Calc()

    def test_0add(self):
        print("run add()")
        self.assertEqual(self.c.add(1, 2, 12), 15, "test add failed")

    def test_1sub(self):
        print("run sub()")
        self.assertEqual(self.c.sub(2, 1, 3), -2, "test sub failed")

    def test_2mul(self):
        print("run mul()")
        self.assertEqual(self.c.mul(2, 3, 5), 30, "test mul failed")

    def test_3div(self):
        print("run div()")
        self.assertEqual(self.c.div(8, 2, 4), 1, "test div failed")

    @unittest.skip("don't run")
    def test4(self):
        print("no start with test")


if __name__ == '__main__':
    unittest.main()
