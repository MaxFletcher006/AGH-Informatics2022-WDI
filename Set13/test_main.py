import main
import unittest
from main import checkingLines

class testingLines(unittest.TestCase):

    '''def setUp(self):

        self.coordinates = [(2, 3), (-3, -1), (2, -1)]
        self.value = False'''
    def test_first_case(self):

        coordinates = [(6,8),(9,1),(3,1)]

        self.assertFalse((checkingLines(coordinates)))

    def test_second_case(self):
        coordinates = [(2,3),(-3,-1),(2,-1)]

        self.assertFalse((checkingLines(coordinates)))

    def test_third_case(self):
        coordinates = [(9,-6),(0,3),(7,4)]

        self.assertFalse((checkingLines(coordinates)))

    def test_fourth_case(self):
        coordinates = [(0,0),(0,0),(0,0)]
        self.assertFalse((checkingLines(coordinates)))

if __name__ == '__main__' :
    unittest.main()



