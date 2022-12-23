class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        left = 0
        right = 0
        len_output = len(word1)+len(word2)
        for x in range(len_output):
            if left <len(word1) and right<len(word2):
                output+=word1[left]
                output+=word2[right]
                left+=1
                right+=1
            elif left == len(word1) and right<len(word2): 
                output+=word2[right]
                right+=1
            elif left < len(word1) and right==len(word2):
                output+=word1[left]
                left+=1
        return output
        