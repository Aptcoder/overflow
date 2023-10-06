import unittest

from solution import compress

class TestCompress(unittest.TestCase):

    def test_compress(self):
        self.assertEqual(compress('bbcceeee'), 'b2c2e4')
        self.assertEqual(compress('aaabbbcccaaa'), 'a3b3c3a3')
        self.assertEqual(compress('a'), 'a')
        self.assertEqual(compress('abcd'), 'abcd')
        self.assertEqual(compress('aabcd'), 'a2b1c1d1')



if __name__ == "__main__":
    unittest.main()
