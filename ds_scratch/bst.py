class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Bst:
    def __init__(self, nodes=None):
        if nodes:
            self.construct(nodes)
        else:
            self.nodes = nodes
    def construct(self, vals):
        mid = len(vals) // 2
        base = Node(vals[mid])
        l_side = base
        r_side = base
        for i in range(mid - 1, -1, -1):
            node = Node(vals[i])
            l_side.left = node
            l_side = l_side.left
        for i in range(mid + 1, len(vals)):
            r_side.right = Node(vals[i])
            r_side = r_side.right
        self.nodes = base
       

    def __len__(self):
        def helper(node):
            if not node:
                return 0
            else:
                return max([helper(node.left),helper(node.right)]) + 1
        return helper(self.nodes)

    def min(self):
        def helper(node):
            if not node:
                return None
            else:
                return self.min(node.left) if self.min(node.left) else node.val
        return helper(self.nodes)

        
