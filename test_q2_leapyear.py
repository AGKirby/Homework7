import unittest
import q2_leapyear

class testCaseAdd(unittest.TestCase):
    def test_leapyear1(self): #check that a year divisible by 4 is considered a leap year
        result = q2_leapyear.leapyear(1904)
        self.assertEqual(result, True)

    def test_leapyear2(self): #check that a year divisible by both 4 and 100 is not considered a leap year
        result = q2_leapyear.leapyear(1900)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main(verbosity=2)