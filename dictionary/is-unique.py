# Is unique: check if a string has all unique characters 
import unittest


def unique(str):
    #print(str)
    #hint hash the table  => dict: key-value
    char_set = {}

    for char in str:
        #print(char)
        if char in char_set:
            return False
        char_set[char] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'),('s7281ui'),('')]
    dataF = [('dd231a'),('882ace')]

    def test_unique(self):
        #true check
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
        
        #false check
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)

if __name__ == "__main__":
    unittest.main()