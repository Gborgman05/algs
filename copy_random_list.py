## apparently this node is hashable?

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new = None
        prev = None
        saved = head
        store = {}
        while head:
            if not new:
                new = Node(head.val)
                prev = new
            else:
                prev.next = Node(head.val)
                prev = prev.next
            store[head] = prev
            head = head.next
        head = saved
        curr = new
        while head:
            if head.random:
                curr.random = store[head.random]
            else:
                curr.random = None
            head = head.next
            curr = curr.next
            
        return new
                
        

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new = None
        prev = None
        saved = head
        store = {}
        while head:
            if not new:
                new = Node(head.val)
                prev = new
            else:
                prev.next = Node(head.val)
                prev = prev.next
            store[prev.val] = prev
            head = head.next
        head = saved
        curr = new
        while head:
            if head.random:
                curr.random = store[head.random.val]
            else:
                curr.random = None
            head = head.next
            curr = curr.next
            
        return new
                
        # works if val is unique