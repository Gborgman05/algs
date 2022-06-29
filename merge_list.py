# Definition for singly-linked list.
# import pdb
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # saved = l1
        # first = True
        # while l1 and
        # if l2.val =< l1.val:
        #     if first:
        #         then = l2.next
        #         l2.next = l1
        #         saved = l2
        #         l2 = then
        # elif l2.val > l1.val:
        #     l1 = l1.next
        head = l1
        last = None
        while l2 or l1:
            if not l2:
                return head
            elif not l1.next and l2.val > l1.val:
                l1.next = l2
                return head
            elif l2.val <= l1.val:
                start = l2
                end = l2
                while end.next and end.next.val <= l1.val:
                    end = end.next
                l2 = end.next
                end.next = l1
                if last:
                    last = l1
                else:
                    head = start
                    last = l1
            elif l2.val > l1.val:
                l1 = l1.next
                last = l1
        return head
        
                
def make_list(lst):
    head = None
    nxt = None
    for item in lst:
        if not head:
            head = ListNode(item)
            nxt = head
        else:
            nxt.next = ListNode(item)
            nxt = nxt.next
    return head
driver = Solution()
print(driver.mergeTwoLists(make_list([1, 2, 4]), make_list([1, 3, 4])))


            
        