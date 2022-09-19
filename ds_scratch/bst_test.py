# tests for bsts
import unittest
from bst import Bst

class TestLlist(unittest.TestCase):

    def test_create(self):
        a = Bst()
        self.assertEqual(a.nodes, None)
        b = Bst([1, 2, 3])
        self.assertEqual(b.nodes.val, 2)