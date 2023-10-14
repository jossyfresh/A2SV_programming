class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        maps = {chr(i+97):i+1 for i in range(26)}
        arr = [1]
        for i in range(k):
            val = arr[-1] * power
            arr.append(val)
        hashfind = 0
        for i in range(k):
            hashfind += (arr[i] * (maps[s[i]]))
        l = 0
        r = k
        j = 0
        while r < len(s):
            if hashfind % modulo == hashValue:
                return s[l:r]
            hashfind -= maps[s[l]] * arr[j]
            hashfind //= power
            hashfind += maps[s[r]] * arr[k-1]
            r += 1
            l += 1
        if hashfind%modulo == hashValue:
            return s[l:r]

        return