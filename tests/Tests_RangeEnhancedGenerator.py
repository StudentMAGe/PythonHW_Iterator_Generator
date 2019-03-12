import unittest
from RangeEnhancedIterator_Generator import GeneratorEnhancedRange


class GeneratorTests(unittest.TestCase):

    def test_on_range_w_one_arg(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2)], [0, 1])

    def test_on_range_w_two_args(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2, 5)], [2, 3, 4])

    def test_on_range_w_three_args(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2, 7, 2)], [2, 4, 6])


if __name__ == '__main__':
    unittest.main()
    
    
