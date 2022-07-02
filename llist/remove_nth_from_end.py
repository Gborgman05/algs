# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        saved = head
        iterator = 0
        length = 0
        while head:
            length += 1
            head = head.next
        n = length - n
        head = saved
        if n == 0:
            return saved.next
        while head:
            if iterator + 1 == n:
                head.next = head.next.next
                return saved
            else:
                head = head.next
                iterator += 1