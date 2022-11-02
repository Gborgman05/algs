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
        arr = []
        q = [root]
        if q == [None]:
            return "[]"
        while q:
            cur = q.pop(0)
            if cur:
                arr.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                arr.append(cur)
        while arr[-1] == None:
            arr.pop()
        # print(arr)
        out = "["
        for i in range(len(arr)):
            if arr[i]:
                out += str(arr[i]) + ","
            else:
                out += "null,"
        out = out[:-1] + "]"
        print(out)
        return out
            
    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        def calc_children(index):
            if "null" in info:
                index = min(index, info.index("null"))
                if info[index] == "null":
                    info[index] = None
            return 2*index + 1, 2*index + 2

        info = [char.strip("[]") for char in data.split(",")]
        cur_index = 0
        if info[0] == None:
            return None
        def helper(cur_index):
            root = TreeNode(info[cur_index])       
            l_ind, r_ind = calc_children(cur_index)
            if l_ind < len(info) and info[l_ind] != "null" and info[l_ind]:
                root.left = helper(l_ind)
            if r_ind < len(info) and info[r_ind] != "null" and info[r_ind]:
                root.right = helper(r_ind)
            return root
        return helper(0)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))