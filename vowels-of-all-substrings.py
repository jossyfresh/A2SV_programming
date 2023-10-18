class Solution:
    def countVowels(self, word: str) -> int:
        vow = "aeiou"
        ans = 0
        for i in range(len(word)):
            if word[i] in vow:
                ans += (i+1) * (len(word)-i)
        return ans