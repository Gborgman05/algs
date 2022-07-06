class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if not head.next:
                return head
            else:
                saved = self.reverseList(head.next)
                a = saved
                while a.next:
                    a = a.next
                a.next = ListNode(head.val)
                return saved