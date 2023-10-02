class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.eow = True
    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)-1):
            ch = word[i]
            if ch in node.children and node.children[ch].eow:
                node = node.children[ch]
            else:
                return False
        return True
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        words.sort(key=lambda x:len(x))
        if len(words[0]) > 1:
            return ""
        ans = words[0]
        trie.insert(words[0])
        for i in range(1,len(words)):
            if trie.search(words[i]):
                if len(ans) < len(words[i]):
                    ans = words[i]
            trie.insert(words[i])
        return ans