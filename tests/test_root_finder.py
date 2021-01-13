import unittest

#from .context import src
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
pdir = os.path.dirname(currentdir)
ppdir = os.path.dirname(pdir)
sys.path.append(pdir)
sys.path.append(ppdir)

from src.route_finder import Route_finder

class TestCommon(unittest.TestCase):

    def setUp(self):
        self.commonclass = Route_finder()

    def test_print(self):
        """
        This is a fake test
        """
        print("This is a fake test for Root_finder class ")
        #self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
