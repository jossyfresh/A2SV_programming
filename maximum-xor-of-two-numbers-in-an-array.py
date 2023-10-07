class TrieNode :
    def __init__(self):
        self.children = {}

class Trie :
    def __init__(self) :
        self.root = {}
    def insert(self, n) :
        temp = self.root
        i = 31
        while i >= 0 :
            bit = (n >> i) & 1
            if bit not in temp:
                temp[bit] = {}
            temp = temp[bit]
            i -= 1
    def xor(self, value) :
        temp = self.root
        current_ans = 0
        i = 31
        while i >= 0:
            bit = (value >> i) & 1
            if bit^1 in temp:
                temp = temp[bit^1]
                current_ans += (1 << i)
            else:
                temp = temp[bit]
            i -= 1
        return current_ans

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_val = 0
        trie.insert(nums[0])
        for n in nums[1:]:
            max_val = max(trie.xor(n),max_val)
            trie.insert(n)
        return max_val