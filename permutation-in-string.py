class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = Counter(s1)
        window = {}
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i],0)+1
        print(window)
        r = len(s1)
        l = 0
        while r < len(s2):
            if window == target:
                return True
            window[s2[r]] = window.get(s2[r],0)+1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                window.pop(s2[l])
            r+=1
            l+=1
        if window == target:
            return True
        return False