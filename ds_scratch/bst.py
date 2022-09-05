class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class bst:
    def __init__(self, nodes=None):
        if nodes:
            self.construct(nodes)
        else:
            self.nodes = nodes
    def construct(self, nodes):
        pass
