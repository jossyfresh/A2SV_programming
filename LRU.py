class LRUCache:

    def __init__(self, capacity: int):
        self.LRUcache = {}
        self.max_ = capacity
        
    def get(self, key: int) -> int:
        if key not in self.LRUcache:
            return -1
        
        self.LRUcache[key] = self.LRUcache.pop(key)
        return self.LRUcache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LRUcache:
            self.LRUcache.pop(key)
        else:
            if self.max_:
                self.max_ -= 1
            else:
                self.LRUcache.pop(next(iter(self.LRUcache)))
        self.LRUcache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)