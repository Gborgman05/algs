# swaps neighboring nodes recursively
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            rest = self.swapPairs(head.next.next)
            new_head = head.next
            new_head.next = head
            head.next = rest
            return new_head