# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        evens = []
        translocutor = head
        while translocutor.next != None:
            evens.append(translocutor.next)
            translocutor.next = translocutor.next.next
            if translocutor.next != None:
                translocutor = translocutor.next
                continue
            else:
                break
        # print(evens)
        # print(head)
        transverser = head
        while transverser.next != None:
            transverser = transverser.next
        for elem in evens:
            transverser.next = elem
            transverser = transverser.next
        transverser.next = None
        return head