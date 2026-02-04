# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        saved = None
        head = None
        while list1 and list2:
            if not head:
                if list1.val < list2.val:
                    head = list1
                    saved = head
                    list1=list1.next
                else:
                    head = list2
                    saved = head
                    list2=list2.next
            else:
                if list1.val < list2.val:
                    head.next = list1
                    list1=list1.next
                    head = head.next
                else:
                    head.next = list2
                    list2=list2.next
                    head = head.next
        while list1:
            if not head:
                head = list1
                saved = head
                list1=list1.next
            else:
                head.next = list1
                list1=list1.next
                head = head.next
        while list2:
            if not head:
                head = list2
                saved = head
                list2=list2.next
            else:
                head.next = list2
                list2=list2.next
                head = head.next
        return saved
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        saved = head
        while list1 and list2:
            if list1.val < list2.val:
                tmp = list1
                list1 = list1.next
                head.next = tmp
                head = head.next
            else:
                tmp = list2
                list2 = list2.next
                head.next = tmp
                head = head.next
        if not head:
            if not list2:
                return list1
            if not list1:
                return list2
        else:
            if list1:
                head.next = list1
            elif list2:
                head.next = list2
        return saved.next