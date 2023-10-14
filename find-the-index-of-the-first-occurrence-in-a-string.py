class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        maps = {chr(i+97):i+1 for i in range(26)}
        a = 26
        hash = 0
        if len(needle) > len(haystack):
            return -1
        t = len(needle)-1
        for i in range(len(needle)):
            hash += maps[needle[i]] * 26 ** t
            t -= 1
        hashfind = 0
        t = len(needle)-1
        for i in range(len(needle)):
            hashfind += maps[haystack[i]] * 26 ** t
            t -= 1
        l = 0
        r = len(needle)
        t = len(needle)-1
        while r < len(haystack):
            if hashfind == hash:
                return l
            hashfind -= (maps[haystack[l]] * 26 ** t)
            hashfind *= 26 
            hashfind += maps[haystack[r]]
            l += 1
            r += 1
        if hash == hashfind:
            return l
        return -1