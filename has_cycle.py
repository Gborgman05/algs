# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p_1 = head
        p_2 = head
        slow = False
        while p_1:
            p_1 = p_1.next
            if not slow:
                slow = True
            else:
                slow = False
                p_2 = p_2.next
            if p_1 == p_2:
                return True
        return False