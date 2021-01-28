import unittest
from slubard import *

class TestSluBardFunctions(unittest.TestCase):
    
    def test_my_upper(self):
        self.assertEqual(my_upper('SluBard'), 'SLUBARD')
        
    def test_my_lower(self):
        self.assertEqual(my_lower('SluBard'), 'slubard')

if __name__ == '__main__':
    unittest.main()