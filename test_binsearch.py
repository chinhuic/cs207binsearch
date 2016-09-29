
from binsearch import binary_search
import unittest
import numbers
import numpy as np
from fractions import Fraction

input1 = range(10)
input2 = [20, 23, 23, 45, 45, 78, 79]

class MyTest(unittest.TestCase):
    # all of them have test_xxx so that unittest main can run it
    
    def test_value_found_normal_array(self):
        self.assertEqual(binary_search(input1, 5),5)
    
    def test_value_found_single_element_array(self):
        self.assertEqual(binary_search([5], 5),0)
    
    def test_value_found_dup(self):
        self.assertIn(binary_search(input2, 23), (1,2))
        self.assertIn(binary_search(input2, 45), (3,4))
    
    def test_value_not_found_left_bound(self):
        self.assertEqual(binary_search(input1, -5.5),-1)
        
    def test_value_not_found_right_bound(self):
        self.assertEqual(binary_search(input1, 50),-1)
        
    def test_value_not_found_left_bound_single_element_array(self):
        self.assertEqual(binary_search([5], -2),-1)
    
    def test_with_inf_found_normal_needle(self):
        self.assertEqual(binary_search([1,2, np.inf], 2),1)
        
    def test_with_inf_found_inf_needle(self):
        self.assertEqual(binary_search([1, 2, 5 , 6,8 , np.inf], np.inf), 5)
    
    def test_with_inf_not_found_left_bound(self):
        self.assertEqual(binary_search([1,np.inf, 2, 5 , 6], -4), -1)
        
    def test_with_inf_not_found_right_bound(self):
        self.assertEqual(binary_search([1,np.inf, 2, 5 , 6], 10), -1)
        
    def test_with_NaN_found_normal_needle(self):
        self.assertEqual(binary_search([np.nan, 2, 5 , 6], 2),1)
    
    def test_with_NaN_found_NaN_needle(self):
        self.assertTrue(binary_search([np.nan, 2, 5 , 6], np.nan), numbers.Real)
    
    def test_with_NaN_not_found_left_bound(self):
        self.assertEqual(binary_search([1,np.nan, 2, 5 , 6], -4), -1)
        
    def test_with_NaN_not_found_right_bound(self):
        self.assertEqual(binary_search([1,np.nan, 2, 5 , 6], 10), -1)
        
    def test_with_left_right_parameters_not_found(self):
        self.assertEqual(binary_search(input1, 5, 1, 3), -1)
    def test_with_left_right_parameters_found(self):
        self.assertEqual(binary_search(input1, 2, 1, 3), 2)
    def test_with_left_right_parameters_incorrect_order(self):
        self.assertEqual(binary_search(input1, 2, 3, 1), -1)
    def test_with_same_left_right_parameters_found(self):
        self.assertEqual(binary_search(input1, 2, 2, 2), 2)
    def test_with_same_left_right_parameters_not_found(self):
        self.assertEqual(binary_search(input1, 5, 2, 2), -1)
        
    def test_with_empty_array(self):
        self.assertEqual(binary_search([], 5),-1)
        
    def test_char(self):
        with self.assertRaises(TypeError):
            binary_search(['a', 6], 7)
            
    def test_char(self):
        with self.assertRaises(TypeError):
            binary_search([2, 6], 'a')
            
    def test_with_fraction_normal_needle(self):
        self.assertEqual(binary_search([Fraction(1,6),Fraction(7/9), 5, 10 ], 5), 2)

    def test_with_fraction_fraction_needle(self):
        self.assertEqual(binary_search([Fraction(1,6),Fraction(7/9), 5, 10 ], Fraction(1,6)), 0)
        

if __name__ == '__main__':
    unittest.main()