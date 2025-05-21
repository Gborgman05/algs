# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder
        #node, left, right
        #in order
        #left, node, right

        store = {}
        for i in range(len(inorder)):
            store[inorder[i]] = i
        q = deque(preorder)
        def build(start, end):
            if start > end:
                return None
            tmp = q.popleft()
            node = TreeNode(tmp)
            node.left = build(start, store[tmp] -1)
            node.right = build(store[tmp] + 1, end)
            return node
        return build(0, len(preorder)-1)
            