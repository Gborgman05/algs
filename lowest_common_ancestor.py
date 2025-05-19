# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # check left, right for either of the nodes
        def find_either(node, p, q):
            if node:
                if node.val == p.val:
                    return p
                elif node.val == q.val:
                    return q
                else:
                    tmp = find_either(node.left, p, q)
                    if tmp:
                        return tmp
                    else:
                        return find_either(node.right, p, q)
        if not root:
            return None
        else:
            l = find_either(root.left, p, q)
            r = find_either(root.right, p, q)
            if (l and r) or((l or r) and (root.val == p.val or root.val == q.val)) : 
                # this means node is ancestor to two different targets, or it is a target and has one target as descendent
                return root
            elif not l and not r:
                return None
            elif l:
                return self.lowestCommonAncestor(root.left, p, q)
            elif r:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                assert False