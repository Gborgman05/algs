# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def find_len(hd):
            cnter = 1
            if not hd:
                return (0, None)
            while hd.next:
                cnter += 1
                hd = hd.next
            return (cnter, hd)
        llen, end = find_len(head)
        if llen < 2:
            return head
        offset = (llen - k) % llen
        saved = head
        counter = 0
        prev = None
        while counter < offset:
            prev = head
            head = head.next
            counter += 1
        if prev:
            prev.next = None
            end.next = saved

        return head