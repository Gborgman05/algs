# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, head)
        saved = head
        while head and head.next and head.next.next:
            if head.next.val == head.next.next.val:
                tmp = head.next.next
                while tmp:
                    if tmp.next and tmp.next.val == head.next.val:
                        tmp = tmp.next
                    else:
                        break
                head.next = tmp.next
            else:
                head = head.next
        return saved.next
# quickly modified from deleting just one