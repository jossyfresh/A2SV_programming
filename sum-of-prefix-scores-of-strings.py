class TrieNode:
    def __init__(self,val):
        self.children = [None for i in range(26)]
        self.eow = False
        self.val = val
        self.let = ""
class Trie:
    def __init__(self):
        self.root = TrieNode(0)
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if node.children[indx] == None:
                node.children[indx] = TrieNode(1)
            else:
                node.children[indx].val += 1
            node.children[indx].let = ch
            node = node.children[indx]
        node.eow = True
    def search(self,word):
        ans = 0
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if node.children[indx] != None:
                node = node.children[indx]
                ans += node.val
            else:
                return ans
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for x in words:
            trie.insert(x)
        ans = []
        for x in words:
            val = trie.search(x)
            print(val,x)
            ans.append(val)
        return ans