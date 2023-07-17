import unittest
from twoSum import twoSum

class MyTestCase(unittest.TestCase):
    def test_1(self):
        result = twoSum([2,7,11,15],9)
        self.assertEqual(result, [0,1])
    def test_2(self):
        result = twoSum([3,3],5)
        self.assertEqual(result, [0,1])


if __name__ == '__main__':
    unittest.main()