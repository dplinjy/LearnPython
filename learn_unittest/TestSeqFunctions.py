import random, sys, unittest


class TestSeqFunctions(unittest.TestCase):
    a = 6

    def setUp(self):
        self.seq = list(range(20))

    @unittest.skip("skipping")
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(20)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    @unittest.skipIf(a>5, "condition is not satisfied!")
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    @unittest.skipUnless(sys.platform.startswith("linux"), "require linux environment")
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()