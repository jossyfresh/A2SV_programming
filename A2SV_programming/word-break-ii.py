class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.val = ""

class Trie:
    def __init__(self,words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.eow = True
        node.val = word
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie(wordDict)
        ans = []
        
        def dpSearch(word,node,val):
            if not word:
                ans.append(val)
                return 
            for i in range(len(word)):
                ch = word[i]
                if ch in node.children:
                    node = node.children[ch]
                else:
                    return 
                if node.eow:
                    dpSearch(word[i+1:],trie.root,val + [node.val])
            return 
        dpSearch(s,trie.root,[])
        for i in range(len(ans)):
            ans[i] = " ".join(ans[i])
        return ans  
