# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # seen = []
        while headA:
            headA.seen = True
            # seen.append(headA)
            headA = headA.next
        while headB:
            if hasattr(headB, "seen"):
                return headB
            else:
                headB = headB.next
        