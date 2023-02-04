class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        bool = False
        map1 = {}
        for x in s1:
            map1[x] = map1.get(x,0)+1
        map2 = {}
        if len(s1) > len(s2):
            return False
        else:
            l = 0
            r = len(s1)
            for x in range(len(s1)):
                map2[s2[x]] = map2.get(s2[x],0) + 1
            while r <= len(s2):
                if map1 == map2:
                    bool = True
                    break
                if r == len(s2):
                    break
                map2[s2[r]] = map2.get(s2[r],0)+1
                if map2.get(s2[l]) == 1:
                    map2.pop(s2[l])  
                else:
                    map2[s2[l]] = map2.get(s2[l],0) -1
                l+=1
                r+=1
        return bool
