class ListNode:
    def __init__(self, val, prev=None, then=None):
        self.next = then
        self.val = val

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr1 = head
        ptr2 = head
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if not ptr2 or not ptr1:
                return False
            else:
                ptr2 = ptr2.next
            if ptr1 == ptr2:
                return True
        return False

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
print(driver.hasCycle(make_list([1, 3, 4])))
