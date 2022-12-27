# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q1 = []
        q2 = []
        if root is None or root.left == root.right and root.left == None:
            return True
        else:
            q1.append(root.left)
            q2.append(root.right)
        while len(q1) > 0 and len(q2) > 0:
            if len(q1) != len(q1):
                return False
            l = q1.pop(0)
            r = q2.pop(0)
            print(l.val)
            print(r.val)
            if l == None or r == None:
                if l == r:
                    continue
                else:
                    return False
            elif l.val == r.val:
                q1.append(l.left)
                q1.append(l.right)
                q2.append(l.right)
                q2.append(l.left)
            else:
                return False
                
                
        return q1 == q2
            
            
                    
                
                
            
        