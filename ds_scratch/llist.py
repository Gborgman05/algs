# Galen Borgman
# 8/17/2022
# linked list 
import pdb
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
    def pop(self, index=None):
        # pdb.set_trace()
        if index == None and self.len < 1:
            raise BaseException("Attempted to pop from empty list")
        if index is None:
            index = self.len - 1
        if index >= self.len or index < 0 :
            raise BaseException("Attempted to pop from index out of range")
        if index == 0:
            tmp = self.nodes.val 
            if self.nodes:
                self.nodes = self.nodes.n
            # self.nodes = self.nodes.next if self.nodes else None
            self.len -= 1
            return tmp
        counter = 1
        curr = self.nodes
        nxt = self.nodes.n if self.nodes else None
        while counter < index:
            curr = nxt
            nxt = curr.n
            counter += 1
        if nxt:
            # i wonder if this is garbage collected, removed the only 
            # forward reference to a node, but the node has a reference to active code. 
            # It should be garbage collected
            tmp = curr.nxt.val
            curr.nxt = curr.nxt.n
            return tmp
        else:
            raise BaseException("Attempted to pop from index out of range")



    def __len__(self):
        return self.len

    def lookup(self, i):
        cur = self.nodes
        while i > 0:
            cur = cur.n
            i -= 1
        return cur.val








                

