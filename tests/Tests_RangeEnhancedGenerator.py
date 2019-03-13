import unittest
from RangeEnhancedIterator_Generator import GeneratorEnhancedRange


class GeneratorTests(unittest.TestCase):

    def test_on_range_w_one_arg(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2)], [0, 1])

    def test_on_range_w_two_args(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2, 5)], [2, 3, 4])

    def test_on_range_w_three_args(self):
        self.assertEqual([n for n in GeneratorEnhancedRange(2, 7, 2)], [2, 4, 6])
        
    def test_on_nonnumeric_args(self):
        with self.assertRaises(Exception, msg = "Arguments must be numeric"):
            example = GeneratorEnhancedRange(5, "o", -1)

    def test_on_zero_step(self):
        with self.assertRaises(Exception, msg = "Unable to range with step = 0"):
            example = GeneratorEnhancedRange(5, 6, 0)

    def test_on_wrong_number_of_args(self):
        with self.assertRaises(Exception,
                msg = "GeneratorEnhancedRange requires at least one, but no more than three arguments"):
            example = GeneratorEnhancedRange()
        with self.assertRaises(Exception,
                msg = "GeneratorEnhancedRange requires at least one, but no more than three arguments"):
            example = GeneratorEnhancedRange(2, 7, 2, 0)


if __name__ == '__main__':
    unittest.main()
    
    
