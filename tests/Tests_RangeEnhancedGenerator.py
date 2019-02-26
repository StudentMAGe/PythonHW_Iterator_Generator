
# coding: utf-8

# In[ ]:


import unittest
import RangeEnhancedIterator_Generator
from RangeEnhancedIterator_Generator import GeneratorEnhancedRange


class GeneratorTests(unittest.TestCase):

    def setUp(self):
        print ('Setup called')
    
    def test_on_range_w_one_arg(self):
        example = GeneratorEnhancedRange(2)
        s = []
        for i in range(10):
            for i in example():
                s.append(i)
        self.assertEqual(s, [0, 1])
    
    def test_on_range_w_two_args(self):
        example = GeneratorEnhancedRange(2,5)
        s = []
        for i in range(10):
            for i in example():
                s.append(i)
        self.assertEqual(s, [2, 3, 4])
            
    def test_on_range_w_three_args(self):
        example = GeneratorEnhancedRange(2, 7, 2)
        s = []
        for i in range(10):
            for i in example():
                s.append(i)
        self.assertEqual(s, [2, 4, 6])
          
    def tearDown(self):
        print ('Tear down called')


if __name__ == '__main__':
    unittest.main()


