class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            nxt = head.next
            head.next = node
            node = head
            head = nxt
        return node

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = None
        while head:
            tmp = head.next
            head.next = nxt
            nxt = head
            head = tmp
        return nxt