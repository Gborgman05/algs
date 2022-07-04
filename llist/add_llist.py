# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = 1
        value = 0
        carry = 0
        while True:
            if l1 and l2:
                sub_sum = l1.val + l2.val + carry
                if sub_sum < 10:
                    value += sub_sum * digit
                    digit *= 10
                    l1 = l1.next
                    l2 = l2.next
                    carry = 0
                else:
                    carry = 1
                    sub_sum -= 10
                    value += sub_sum * digit
                    digit *= 10
                    l1 = l1.next
                    l2 = l2.next
                    
            elif l1:
                while l1:
                    sub_sum = l1.val + carry
                    if sub_sum < 10:
                        carry = 0
                    else:
                        sub_sum -= 10
                        carry = 1
                    value += digit * sub_sum
                    digit *= 10                                            
                    l1 = l1.next
            elif l2:
                while l2:
                    sub_sum = (l2.val + carry)
                    if sub_sum < 10:
                        carry = 0
                    else:
                        sub_sum -= 10
                        carry = 1
                    value += digit * sub_sum
                    digit *= 10
                    l2 = l2.next
            else:
                return value
                    
        