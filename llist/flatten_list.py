# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        saved = head
        def sub_flatten(ptr):
            start = ptr
            while ptr:
                if ptr.child:
                    child_start, child_end = sub_flatten(ptr.child)
                    child_end.next = ptr.next
                    if ptr.next:
                        ptr.next.prev = child_end
                    ptr.next = child_start
                    child_start.prev = ptr
                    ptr.child = None
                    ptr = child_end
                else:
                    if not ptr.next:
                        break
                    ptr = ptr.next
            return start, ptr
        st, end = sub_flatten(head)
        return st