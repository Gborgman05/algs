# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(lst):
            l = 0
            while lst:
                l += 1
                lst = lst.next
            return l
        l1len = get_length(l1)
        l2len = get_length(l2)
        cumsum = 0
        while l1 or l2:
            cumsum *=10
            if l1len > l2len:
                cumsum += l1.val
                l1len -= 1
                l1 = l1.next
            elif l1len < l2len:
                cumsum += l2.val
                l2len -= 1
                l2 = l2.next
            else:
                cumsum += l1.val + l2.val
                l1len -= 1
                l2len -= 1
                l1 = l1.next
                l2 = l2.next
        def decon(num):
            new = [ListNode(i) for i in list(str(num))]
            for i in range(len(new) - 1):
                new[i].next = new[i+1]
            print(new)
            return new[0]
        return decon(cumsum)