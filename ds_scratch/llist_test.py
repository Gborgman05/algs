# Galen Borgman
# 5/28/2022
# Test cases

import unittest
from llist import Llist

class TestLlist(unittest.TestCase):

    def test_create(self):
        my_list = Llist()
        self.assertEqual(0, len(my_list))
        new_list = Llist([1, 2, 3, 4])
        self.assertEqual(4, len(new_list))
    
    def test_append(self):
        my_list = Llist()
        self.assertEqual(0, len(my_list))
        my_list.append(0)
        self.assertEqual(1, len(my_list))
        new_list = Llist([1, 2, 3, 4])
        self.assertEqual(4, len(new_list))
        new_list.append(5)
        self.assertEqual(5, len(new_list))

    def test_pop(self):
        my_list = Llist()
        my_list.append(0)
        self.assertEqual(0, my_list.pop())
        new_list = Llist([1, 2, 3, 4])

    def test_push_pop(self):
        my_list = Llist()
        my_list.append(0)
        self.assertEqual(0, my_list.pop())
        my_list.append(11)
        self.assertEqual(11, my_list.pop())
    
    def test_lookup(self):
        lst = [1, 3, 4, 5, 6]
        my_list = Llist(lst)
        for i in range(len(lst)): 
            self.assertEqual(lst[i], my_list[i])

    def test_set(self):
        lst = [1, 3, 4, 5, 6]
        my_list = Llist(lst)
        for i in range(len(lst)): 
            self.assertEqual(lst[i], my_list[i])
        my_list[1] = -10
        new = [1, -10, 4, 5, 6]
        for i in range(len(new)):
            self.assertEqual(my_list[i], new[i])
    
    def test_extensive(self):
        # lst = []
        my_list = Llist()
        for i in [2, 3, 4 -1, 2]:
            my_list.append(i)
        for i in [0, 1, 2]:
            my_list[i] = i
        test = [0, 1, 2, -1, 2]
        for i in range(len(test)):
            print(i)
            self.assertEqual(test[i], my_list[i])

