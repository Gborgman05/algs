# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        saved = []
        while head:
            saved.append(head.val)
            head = head.next
        i = 0
        j = len(saved) - 1
        while i < j:
            if saved[i] != saved[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
            