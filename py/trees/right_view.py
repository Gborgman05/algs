# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root:
            level = [root]
            while level:
                view.append(level[-1].val)
                # level = [kid for kid in [[node.left, node.right] for node in level] if kid]
                candidates = []
                for node in level:
                    if node.left:
                        candidates.append(node.left)
                    if node.right:
                        candidates.append(node.right)
                level = candidates
                    
        return view