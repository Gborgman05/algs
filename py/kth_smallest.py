# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def get_count(node):
        #     """
        #     gets the count of nodes in that subtree
        #     """
        #     if not node:
        #         return 0
        #     else:
        #         return get_count(node.left) + get_count(node.right) + 1
        # sum_so_far = 0
        # while True:
        #     count = get_count(root.left) + sum_so_far
        #     if k == count:
        #         return root.left
        #     elif k < count:
        #         root = root.left
        #     elif k == count + 1:
        #         return root
        #     else: 
        #         sum_so_far += count + 1
        #         root = root.right
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = []
        def helper(node):
            if node is None or len(cnt) > k:
                return
            else:
                helper(node.left)
                cnt.append(node.val)
                helper(node.right)
        helper(root)
        return cnt[k-1]

                