class TrieNode:
    def __init__(self):
        self.children = [None for i in range(27)]
        self.eow = False
        self.value = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word,i) -> None:
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if ch == "{":
                indx = 26
            if node.children[indx] == None:
                node.children[indx] = TrieNode()
            node.children[indx].value = i
            node = node.children[indx]
        node.eow = True
    def search(self,word):
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if ch == "{":
                indx = 26
            if node.children[indx] != None:
                node = node.children[indx]
            else:
                return -1
        return node.value
class WordFilter:
    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        for i in range(len(self.words)):
            x = self.words[i]
            for j in range(len(x)):
                val = x[j:] + "{" + x
                self.trie.insert(val,i)
    def f(self, pref: str, suff: str) -> int:
        ans = self.trie.search(suff + "{" + pref)
        return ans
        

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)