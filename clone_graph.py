"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        q = []
        seen = []
        copied = {}
        if node:
            q.append(node)
        while len(q) > 0:
            my_node = q.pop(0)
            # print(seen, " seen")
            # print(my_node.val, " current")
            if not my_node or my_node.val in seen:
                pass
            else:
                seen.append(my_node.val)
                copied[my_node.val] = Node(my_node.val)
                q += my_node.neighbors #[neighbor for neighbor in my_node.neighbors if neighbor.val not in seen]
        if node:
            q.append(node) 
            seen = []
        while len(q) > 0:
            my_node = q.pop(0)
            if not my_node or my_node.val in seen:
                pass
            else:
                # print([neighbor_node.val for neighbor_node in my_node.neighbors])
                # print([copied[neighbor_node.val] for neighbor_node in my_node.neighbors])
                copied[my_node.val].neighbors = [copied[neighbor_node.val] for neighbor_node in my_node.neighbors]
                # print('after')
                # print(copied[my_node.val].neighbors)
                seen.append(my_node.val)
                q += my_node.neighbors
        # print(copied[1].val, " val ", [n.val for n in copied[1].neighbors])
        if copied:
            return copied[1]
        

        """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}
        q = []
        if node:
            q.append(node)
        while q:
            curr = q.pop(0)
            if not curr or curr.val in seen:
                continue
            seen[curr.val] = Node(curr.val)
            q += curr.neighbors
        if node:
            q = [node]
        connected = {}
        while q:
            curr = q.pop(0)
            if not curr or curr.val in connected:
                continue
            q += curr.neighbors
            seen[curr.val].neighbors = [seen[n.val] for n in curr.neighbors]
            connected[curr.val] = 1
        
        return seen[node.val]
