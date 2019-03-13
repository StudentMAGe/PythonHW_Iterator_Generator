import unittest
from RangeEnhancedIterator_Generator import IteratorEnhancedRange


class IteratorTests(unittest.TestCase):
    
    def test_on_range_w_one_arg(self):
        example = IteratorEnhancedRange(2)
        self.assertEqual(next(example), 0)
        self.assertEqual(next(example), 1)
        self.assertRaises(StopIteration, next, example)
    
    def test_on_range_w_two_args(self):
        example = IteratorEnhancedRange(2,5)
        self.assertEqual(next(example), 2)
        self.assertEqual(next(example), 3)
        self.assertEqual(next(example), 4)
        self.assertRaises(StopIteration, next, example)
            
    def test_on_range_w_three_args(self):
        example = IteratorEnhancedRange(2, 7, 2)
        self.assertEqual(next(example), 2)
        self.assertEqual(next(example), 4)
        self.assertEqual(next(example), 6)
        self.assertRaises(StopIteration, next, example)

    def test_on_nonnumeric_args(self):
        with self.assertRaises(Exception, msg = "Arguments must be numeric"):
            example = IteratorEnhancedRange(5, "o", -1)

    def test_on_zero_step(self):
        with self.assertRaises(Exception, msg = "Unable to range with step = 0"):
            example = IteratorEnhancedRange(5, 6, 0)

    def test_on_wrong_number_of_args(self):
        with self.assertRaises(Exception,
                msg = "IteratorEnhancedRange requires at least one, but no more than three arguments"):
            example = IteratorEnhancedRange()
        with self.assertRaises(Exception,
                msg = "IteratorEnhancedRange requires at least one, but no more than three arguments"):
            example = IteratorEnhancedRange(2, 7, 2, 0)

    def tearDown(self):
        print ('Tear down called')


if __name__ == '__main__':
    unittest.main()

