from q import solve
from typing import List, Optional
import unittest

class TestClass(unittest.TestCase):
    def test_0(self):
        file_name = "data_test_0.txt"
        A, B, C, output= solve(file_name)
        expected = "4,6,3,5,6,3,5,2,1,0"
        self.assertEqual(output, expected, "Incorrect")


    def test_1(self):
        #If register C contains 9, the program 2,6 would set register B to 1.
        file_name = "data_test_1.txt"
        A, B, C, output= solve(file_name)
        expected = 1
        self.assertEqual(B, expected, "Incorrect")

    def test_2(self):
        #If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
        file_name = "data_test_2.txt"
        A, B, C, output= solve(file_name)
        expected = "0,1,2"
        self.assertEqual(output, expected, "Incorrect")

    def test_3(self):
        #If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
        file_name = "data_test_3.txt"
        A, B, C, output= solve(file_name)
        expected = "4,2,5,6,7,7,7,7,3,1,0"
        self.assertEqual(output, expected, "Incorrect")
        expected = 0
        self.assertEqual(A, expected, "Incorrect")

    def test_4(self):
        #If register B contains 29, the program 1,7 would set register B to 26.
        file_name = "data_test_4.txt"
        A, B, C, output= solve(file_name)
        expected = 26
        self.assertEqual(B, expected, "Incorrect")

    def test_5(self):
        #If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.
        file_name = "data_test_5.txt"
        A, B, C, output= solve(file_name)
        expected = 44354
        self.assertEqual(B, expected, "Incorrect")

if __name__ == "__main__":
    unittest.main()
