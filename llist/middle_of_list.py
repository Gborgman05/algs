# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        saved = head
        while head:
            head = head.next
            counter += 1
        index = int(counter // 2 + 1) - 1
        print(index)
        while index > 0:
            saved = saved.next
            index -= 1
        return saved
            
            
        