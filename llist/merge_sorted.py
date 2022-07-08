# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        saved = ListNode()
        current = saved
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
        while l1:
            current.next = l1
            current = current.next
            l1 = l1.next
        while l2:
            current.next = l2
            current = current.next
            l2 = l2.next
        return saved.next