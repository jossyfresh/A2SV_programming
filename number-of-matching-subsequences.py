class TrieNode:
    def __init__(self):
        self.childrens = [None for i in range(26)]
        self.isEnd = False
        self.count = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for wordChar in word:
            asciiIndex = ord(wordChar) - ord('a')
            if not node.childrens[asciiIndex]:
                node.childrens[asciiIndex] = TrieNode()
            node = node.childrens[asciiIndex]
        node.isEnd = True
        node.count +=1  
    
    def findIndex(self,word,start,curascii):
        for i in range(start,len(word)):
            if ord(word[i]) - ord('a') == curascii:
                return i
        return -1
    
    def dfsHelper(self,node,word,start):
        for i in range(26):
            if node.childrens[i]:
                child = node.childrens[i]
                index = self.findIndex(word,start,i)
                if index != -1:                    
                    if child.isEnd:
                        self.count += child.count
                    self.dfsHelper(child,word,index+1)
    def dfs(self,word):
        self.count = 0
        self.dfsHelper(self.root,word,0)
        return self.count    

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.insert(word)
        return self.dfs(s)