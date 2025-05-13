# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = None
        carry = False
        curr = None
        while l1 and l2:
            sm = l1.val + l2.val if not carry else l1.val + l2.val + 1
            carry = False
            if sm > 9:
                sm -= 10
                carry = True
            if not curr:
                curr = ListNode(sm)
                final = curr
            else:
                curr.next = ListNode(sm)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sm = l1.val if not carry else l1.val + 1
            carry = False

            if sm > 9:
                sm -= 10
                carry = True
            if not curr:
                curr = ListNode(sm)
                final = curr
            else:
                curr.next = ListNode(sm)
                curr = curr.next
            l1 = l1.next
        while l2:
            sm = l2.val if not carry else l2.val + 1
            carry = False
            if sm > 9:
                sm -= 10
                carry = True
            if not curr:
                curr = ListNode(sm)
                final = curr
            else:
                curr.next = ListNode(sm)
                curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(1)
            curr = curr.next

        return final
        

        