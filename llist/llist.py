class ListNode:
    def __init__(self, val, prev=None, then=None):
        self.next = then
        self.val = val

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