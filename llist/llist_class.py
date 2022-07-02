# My implementaton of a doubly linked list
# https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/
class MyNode:
    def __init__(self, val, prev=None, then=None):
        self.prev = prev
        self.next = then
        self.val = val

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        for i in range(index):
            if not node:
                return -1
            else:
                node = node.next
        if node:
            return node.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head:
            saved = self.head
            self.head = MyNode(val, None, saved)
            saved.prev = self.head
        else:
            self.head = MyNode(val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        if node:
            while node.next:
                node = node.next
            node.next = MyNode(val, node)
        else:
            self.head = MyNode(val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for i in range(index):
            if not node:
                return
            else:
                node = node.next
        if node:
            a = MyNode(val, node.prev, node)
            if node.prev:
                node.prev.next = a
            else:
                self.head = a
            node.prev = a
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0 and self.head:
            self.head = self.head.next
            return
        node = self.head
        for i in range(index):
            if not node:
                return
            else:
                node = node.next
        if node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        else:
            return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)