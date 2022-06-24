# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        saved = head
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        if saved and saved.val == val:
            saved = saved.next
        
        return saved        
                
                
