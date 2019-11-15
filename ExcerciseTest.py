"""Gurpinder Grewal"""
from Excercise4 import display_one
import unittest

print("\nGurpinder Grewal\n")
class TestConnection(unittest.TestCase):
    def test_record(self):
        mylist = display_one()
        trueList = ('1', 'das', 'ad', 'as', 'a', 2)
        self.assertEqual(mylist, trueList)

if __name__ == '__main__':
    unittest.main()
