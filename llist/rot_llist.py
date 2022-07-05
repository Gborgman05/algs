# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        saved = head
        counter = 0
        prev = None
        end = None
        while counter < k:
            if head.next == None:
                head = saved
                counter += 1
                prev = None
                end = head
            else:
                if not prev:
                    prev = head                    
                head = head.next
        if prev:
            prev.next = None
            head.next = save