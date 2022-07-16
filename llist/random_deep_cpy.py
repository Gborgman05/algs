"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# import pdb
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        saved = head
        new = new_ptr = None
        olds = []
        news = []
        while head:
            if not new_ptr:
                new = new_ptr = Node(head.val, None, None)
                # old_new_map.append((head, new_ptr))
                olds.append(head)
                news.append(new_ptr)
            elif new_ptr:
                new_ptr.next = Node(head.val, None, None)
                # old_new_map.append((head, new_ptr))
                olds.append(head)
                new_ptr = new_ptr.next
                news.append(new_ptr)
            head = head.next
        head = saved
        def get_index(ptr, ptr_array):
            for i in range(len(ptr_array)):
                if ptr_array[i] == ptr:
                    return i
            return None
        for i in range(len(olds)):
            old_ptr = olds[i]
            # print(old_ptr.val)
            new_ptr = news[i]
            # print(new_ptr.val)
            index = get_index(old_ptr.random, olds)
            # print(index)
            if index is None:
                new_ptr.random = None
            elif index is not None:
                new_ptr.random = news[index]
        return new
            
            
            
            
        
#         final_list = None
#         hit_null = 0
#         old_nodes_to_new = {}
#         while True:
#             if not final_list:
#                 head = Node(head.val, head.random, head.next)
#                 old_nodes_to_new[head.val] == head
#                 saved = head
#                 if head.next:
#                     head = head.next