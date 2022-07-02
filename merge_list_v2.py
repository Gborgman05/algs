
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        prev = None
        while l1 and l2:
            if l2.val <= l1.val:
                saved = l2.next
                if prev:
                    l2.next = l1
                    prev.next = l2                
                else:
                    l2.next = l1
                    head = l2
                    prev = l1
                l2 = saved
            elif l2.val > l1.val:
                if l1.next:
                    l1 = l1.next
                else:
                    l1.next = l2
                    return head
        return head