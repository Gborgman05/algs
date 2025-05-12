# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        saved = head
        slow = head
        fast = head
        tot_len = 0
        for _ in range(n):
            fast = fast.next
            tot_len += 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            tot_len += 1
        if fast:
            tot_len += 1
        if n == tot_len:
            saved = head.next
            slow = slow.next
        elif slow.next:
            slow.next = slow.next.next
        return saved