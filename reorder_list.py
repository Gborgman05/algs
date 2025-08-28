# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = head
        r = head
        saved_l = l
        saved_r = r
        curr = head
        while curr and curr.next:
            l = l.next
            curr = curr.next.next
        if curr:
            l = l.next
        curr = head
        while curr and curr.next != l:
            curr = curr.next
        curr.next = None
        ## reverse the l list
        saved_reverse = saved_l
        curr = l
        node = None
        while curr:
            tmp = curr.next
            curr.next = node
            if tmp == None:
                break
            node = curr
            curr = tmp
            
        saved = head
        while head and curr:


            tmp = head.next
            head.next = curr
            tmp2 = curr.next
            curr.next = tmp
            curr = tmp2
            head = head.next.next


    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            if fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                fast = fast.next.next
        print(slow)
        # cut and reverse
        later = slow.next
        slow.next = None
        prev = None
        while later:
            tmp = later.next
            .next = curr
            later = later.next
            curr = tmp
        print(curr)
