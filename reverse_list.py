class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            nxt = head.next
            head.next = node
            node = head
            head = nxt
        return node