# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_group(head, k, next):
            node = next
            while head and k > 0:
                tmp = head.next
                head.next = node
                node = head
                head = tmp
                k -= 1
            return node
        saved_head = head
        count = 0
        curr = head
        while head:

            i = 0
            fast = head
            slow = head
            while i < k and fast:
                i+=1
                fast = fast.next
            print(slow)
            print(fast)

            head = reverse_group(slow, k, fast)
            

            # if(count == 0):
            #     saved_head = head
            #     curr = head
            #     i = k
            #     while curr and curr.next and i > 0:
            #         curr = curr.next
            #         i -= 1
            # else:
            #     curr.next=head
            #     i = k
            #     while curr and curr.next and i > 0:
            #         curr = curr.next
            #         i -= 1

                

            count+= 1
            print(head)
            head = fast
            print("saved ", saved_head)
        return saved_head

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## recursive solution
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        node = head
        i = 0
        while curr and i < k:
            i+= 1
            curr = curr.next
        if i == k:
            nxt = self.reverseKGroup(curr, k)

            node = nxt

            while head and k > 0:
                tmp = head.next
                head.next = node
                node = head
                head = tmp
                k -= 1
        return node
