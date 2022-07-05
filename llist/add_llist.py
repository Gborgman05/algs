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

# apparently my solution from ages ago?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         one = []
#         while l1:
#             one.append(l1.val)
#             l1 = l1.next
#         two = []
#         while l2:
#             two.append(l2.val)
#             l2 = l2.next
#         one = one[::-1]
#         two = two[::-1]
#         while len(one) > len(two):
#             two.insert(0, 0)
#         while len(two) > len(one):
#             one.insert(0,0)
#         print(one, two)
            
#         one = one[::-1]
#         two = two[::-1]
#         final_list = []
#         carry = 0
#         for i in range(len(one)):
#             num = one[i] + two[i] + carry
#             carry = 0
#             if num > 9:
#                 #need to carry
#                 carry=1
#                 num -= 10
#             final_list.append(num)
#         if carry:
#             final_list.append(carry)
#         ptr = ListNode()
#         hello = ptr
#         print(final_list)
#         for i in range(len(final_list)):
#             ptr.val = final_list[i]
#             print(final_list[i])
#             if i != len(final_list) - 1:
#                 ptr.next = ListNode()
#                 ptr = ptr.next
#         return hello