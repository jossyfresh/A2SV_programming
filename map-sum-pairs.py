class TrieNode:
    def __init__(self,val = 0):
        self.value = val
        self.children = {}
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)
    def insert(self, key: str, val: int) -> None:
        new = val - self.map[key]
        node = self.root
        self.map[key] = val
        node.value = new
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node.value += new
            node = node.children[ch]
        node.value += new
    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return 0
        return node.value
    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)