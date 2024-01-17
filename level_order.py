# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_order = []
        curr_level_q = []
        todo_q = [root]
        level = 0
        first = True
        while len(todo_q) > 0:
            curr_level_q = todo_q
            level += 1
            todo_q = []
            while len(curr_level_q) > 0:
                node = curr_level_q.pop(0)
                if node:
                    if node.left:
                        todo_q.append(node.left)
                    if node.right:
                        todo_q.append(node.right)
                    if level > len(final_order):
                        final_order.append([node.val])
                    else:
                        final_order[level-1].append(node.val)
        return final_order

            