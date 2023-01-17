class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = 0
        while l < len(names):
            flag = False
            for i in range(len(names)-(l+1)):
                if heights[i] < heights[i+1]:
                    heights[i],heights[i+1] = heights[i+1],heights[i]
                    names[i],names[i+1] = names[i+1],names[i]
                    flag = True
            l+=1
            if not flag: break
        return names