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
    def construct(self, nodes):
        for i in range(len(nodes)):
            pass
    def push(self, item):
        cur = self.nodes
        while cur:
            if item <= cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(item)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(item)
                    break
    def is_valid(self) -> bool:
        """is a valid BST"""
        high = 2147483648 + 1
        low = -2147483648 - 1
        root = self.nodes
        def helper(high, low, node):
            if not node:
                return True
            else:
                return node.val < high and node.val > low and helper(node.val, low, node.left) and helper(high, node.val, node.right)
        return helper(high, low, root)
        
        
            

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

        
