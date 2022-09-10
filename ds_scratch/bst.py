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
        for i in range(len(nodes)):
            pass

    def __len__(self):
        def helper(node):
            if not node:
                return 0
            else:
                return max([helper(node.left),helper(node.right)]) + 1
        return helper(self.nodes)

        
