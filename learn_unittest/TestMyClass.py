# encoding: UTF-8
import unittest

class myclass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-------setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("-------tearDownClass")

    def setUp(self):
        self.a = 3
        self.b = 1
        print("--setUp")

    def test_sum(self):
        self.assertEqual(myclass.sum(self.a, self.b), 4, "test sum failed")

    def test_sub(self):
        self.assertEqual(myclass.sub(self.a, self.b), 2, "test sub failed")


if __name__ == '__main__':
    unittest.main()