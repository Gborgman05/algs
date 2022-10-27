# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr_slow = head
        ptr_fast = head
        while ptr_fast and ptr_fast.next:
            ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next.next
        return ptr_slow