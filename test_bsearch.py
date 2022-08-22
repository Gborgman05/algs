import unittest
from binary_search import bin_search

class TestLlist(unittest.TestCase):
    def test_bsearch(self):
        tst = [5, 6, 7, 8]
        self.assertEqual(bin_search(tst, 5), 0)
        self.assertEqual(bin_search(tst, 6 ), 1)
        self.assertEqual(bin_search(tst, 4), -1)
