class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache = {}
        self.order = []
    def use_item(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.use_item(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if not value:
            value = key
        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.order.pop(0)
            self.cache[key] = value
            self.order.append(key)
            # remove LRU
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)