from llist import ListNode, make_list

class Solution:
    def detectCycle(self, head):
        ptr1 = head
        index = 0
        while ptr1:
            ptr2 = ptr1
            ptr2 = ptr2.next
            seen = {}
            while ptr2:
                if ptr1 == ptr2:
                    return ptr1
                if ptr2 in seen:
                    break
                else:
                    seen[ptr2] = "hi"
                    ptr2 = ptr2.next

            ptr1 = ptr1.next
            index += 1
        return None
driver = Solution()
a = make_list([3,2,0,-4])
b = a
while b.next:
    b = b.next
b.next = a.next
print(driver.detectCycle(a))