class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.curr_size = 0
        self.capacity = capacity
        self.store = {}
        self.latest = Node(0, 0)
        self.oldest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        else:
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        self.store[key] = Node(key, value)
        self.insert(self.store[key])
        if len(self.store) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.store[lru.key]

    def remove(self, node):
        my_node = node
        tmp_left, tmp_right = my_node.prev, my_node.next
        tmp_left.next = tmp_right
        tmp_right.prev = tmp_left
    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)