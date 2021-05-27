import unittest
import q2_leapyear

class testCaseAdd(unittest.TestCase):
    def test_fizzbuzz1(self): #check that the function prints numbers 1 to 100
        result = q2_leapyear.leapyear(1904)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main(verbosity=2)