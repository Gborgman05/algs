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
                    curr.n = node
                    curr = node
                    self.len += 1
                    
                else:
                    self.nodes = node
                    curr = node
                    self.len += 1
    
    def append(self, item):
        # O(n)
        if self.len == 0:
            self.nodes = Node(item)
        else:
            curr = self.nodes
            while curr.n:
                curr = curr.n
            curr.n = Node(item)
        self.len += 1

    def peek(self):
        # O(1)
        if self.len == 0:
            return None
        else:
            # should i retern the value or the node?
            return self.nodes
    def __len__(self):
        return self.len






                

