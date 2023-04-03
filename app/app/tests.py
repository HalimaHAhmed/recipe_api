"""
sample test
"""


from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    
    """ test the calc module."""
    
    def test_add_numbers(self):
        """test adding number together"""
        res = calc.add(5,6)
        self.assertEqual(res,11)
        
    def test_sub_numbers(self):
        """test subtracting number together"""
        res = calc.add(5,6)
        self.assertEqual(res,11)
         