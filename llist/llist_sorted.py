# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst = sorted(lst)
        new = None
        if lst:
            end = None
            for val in lst:
                if not end:
                    new = ListNode(val)
                    end = new
                else:
                    end.next = ListNode(val)
                    end = end.next
        return new
                
        