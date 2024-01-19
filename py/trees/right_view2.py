# done on 01/19/2024 08:59	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #level order traversal right to left
        curr =[]
        if root:
            next_level = [root]
        else:
            next_level = []
        final = []
        while len(next_level) > 0:
            curr = next_level
            next_level = []
            while len(curr) > 0:
                node = curr.pop(0)
                if node:
                    if len(curr) == 0:
                        final.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
        return final
                
        