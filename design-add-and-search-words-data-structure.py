class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.eow = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            indx = ord(ch) - 97
            if node.children[indx] == None:
                node.children[indx] = TrieNode()
            node = node.children[indx]
        node.eow = True
    def search(self,word: str) -> bool:
        node = self.root
        def dfsSearch(node,word):
            if node == None:
                return False
            for i in range(len(word)):
                ch = word[i]
                if ch != ".":
                    indx = ord(ch) - 97
                    if node.children[indx] != None:
                        node = node.children[indx]
                    else:
                        return False
                else:
                    for j in range(len(node.children)):
                        if dfsSearch(node.children[j],word[i+1:]):
                            return True
                    return False
            if not node.eow:
                return False
            return True
        return dfsSearch(node,word)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)