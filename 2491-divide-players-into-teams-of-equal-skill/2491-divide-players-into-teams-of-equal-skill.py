class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if len(skill) == 0:
            return skill[0]*skill[1]
        res =[]
        ans = 0
        l = 0
        r = len(skill)-1
        while l < r:
            res.append(skill[l]+skill[r])
            ans+=skill[l]*skill[r]
            l+=1
            r-=1
        if len(set(res)) > 1:
            return -1
        else:
            return ans