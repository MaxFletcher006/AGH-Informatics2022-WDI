import main
import unittest
from Set9.Zadanie11 import P


class checkingLines(unittest.TestCase):

    def first_case(self):

        coordinates = [(2, 3), (-3, -1), (2, -1)]

        self.assertEqual(P, 6)

if __name__ == '__main__' :
    unittest.main()



