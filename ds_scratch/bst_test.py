# tests for bsts
import unittest
from bst import Bst

class TestLlist(unittest.TestCase):

    def test_create(self):
        a = Bst()
        self.assertEqual(a.nodes, None)
        b = Bst([1, 2, 3])
        self.assertEqual(b.nodes.val, 2)
    
    def test_l_r(self):
        a = Bst([1, 2, 3, 4, 5])
        self.assertEqual(a.nodes.val, 3)

    def test_is_valid(self):
        a = Bst([1, 2, 3, 4, 5])
        self.assertTrue(a.is_valid())

