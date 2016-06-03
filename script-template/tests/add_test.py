import unittest
from add import *

class AddTest(unittest.TestCase):
    def add_1_1_should_be_2_test(self):
        self.assertEqual( add(1,1), 2)
