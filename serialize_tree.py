# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # I'll do a level order traversal, then fill in the empties
        if not root:
            return "[]"
        final = []
        curr = [root]
        while any(curr):
            tmp = []
            #final += curr
            for node in curr:
                if node is None:
                    final.append("null")
                else:
                    final.append(str(node.val))
                    tmp.append(node.left)
                    tmp.append(node.right)
            curr = tmp
        # while final and final[-1] == None:
        #     final.pop()
        final =   "[" + ",".join(final) + "]"

        return final
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data[1:-1].split(",")

        if not data:
            return None
        if data[0] == '':
            return None
        root = TreeNode(int(data[0]))
        q = [root]
        i = 1
        while q and i < len(data):
            node = q.pop(0)
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1
            if i < len(data) and data[i] != "null":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))