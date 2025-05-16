# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final = None
        curr = final
        while any(lists):
            min_val = min([node.val for node in lists if node])
            for i in range(len(lists)):
                if lists[i] and lists[i].val == min_val:
                    if not final:
                        final = ListNode(lists[i].val)
                        curr = final
                    else:
                        curr.next = ListNode(lists[i].val)
                        curr = curr.next
                    lists[i] = lists[i].next
                    ##print(lists)
        return final
        