from llist import ListNode, make_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detCycle(self, ptr, order):
        print([node.val for node in order])
        cycle_nodes = []
        saved = ptr
        while ptr not in cycle_nodes:
            cycle_nodes.append(ptr)
            ptr = ptr.next
        final_nodes = [node for node in order if node in cycle_nodes]
        if final_nodes:
            return final_nodes[0]
        else:
            return None
        

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        order = []
        ptr1 = head
        ptr2 = head
        while ptr1 and ptr2:
            order.append(ptr2)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            order.append(ptr2)

            if not ptr2 or not ptr1:
                return None
            else:
                order.append(ptr2)
                ptr2 = ptr2.next
            if ptr1 == ptr2:
                return self.detCycle(ptr1, order)
        return None