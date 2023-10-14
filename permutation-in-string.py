class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = Counter(s1)
        window = {}
        left = 0
        for indx in range(len(s1)-1):
            window[s2[indx]] = window.get(s2[indx],0)+1
        
        for right in range(len(s1)-1,len(s2)):
            window[s2[right]] = window.get(s2[right],0)+1
            if window == target:
                return True
            window[s2[left]]-=1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left+=1
        return False