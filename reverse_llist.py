# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # store = []
        # while head:
        #     store.append(head)
        #     head = head.next
        # new = None
        # if store:
        #     new = store.pop()
        # saved = new
        # while store:
        #     new.next = store.pop()
        #     new = new.next
        # return saved
        node = None
        while head:
            tmp = head.next
            head.next = node
            node = head
            head = tmp
        return node
            

        