# Galen Borgman
# 8/17/2022
# linked list 
class Node:
    def __init__(self, val=None, n=None):
        self.val = val
        self.n = n

class Llist:
    def __init__(self, lst=None):
        # O(n) because of appends
        self.len = 0
        self.nodes = None
        if lst:
            for val in lst:
                node = Node(val)
                if self.nodes:
                    curr.next = node
                    curr = node
                    self.len += 1
                    
                else:
                    self.nodes = node:
                    curr = node
                    self.len += 1
    
    def append(self, item):
        # O(n)
        if self.len == 0:
            self.nodes = Node(item)
        else:
            curr = self.nodes
            while curr.next:
                curr = curr.next
            curr.next = Node(item)
        self.len += 1






                

