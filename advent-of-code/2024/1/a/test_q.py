from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):

    def test_on_test_data(self):
        with open('test_data.txt', 'r') as test_data:
            line = test_data.readline()
            while line:
                line = test_data.readline()
                
        
        
if __name__ == "__main__":
    unittest.main()
