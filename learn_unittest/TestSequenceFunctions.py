import unittest
import random

class TestSequnceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
        print("setup complete")

    def test_run(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sth(self):
        assert 1==1

    def tearDown(self):
        print("tearDown completed")


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))
        # print('sjfhsjdfh')

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))


if __name__ == '__main__':
    unittest.main()