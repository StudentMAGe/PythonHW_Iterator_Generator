
# coding: utf-8

# In[ ]:


import unittest
import RangeEnhancedIterator_Generator
from RangeEnhancedIterator_Generator import IteratorEnhancedRange


class IteratorTests(unittest.TestCase):

    def setUp(self):
        print ('Setup called')
    
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

    def tearDown(self):
        print ('Tear down called')


if __name__ == '__main__':
    unittest.main()


