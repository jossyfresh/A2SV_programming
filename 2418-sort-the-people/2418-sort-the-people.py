class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        diction = {}
        for i,x in enumerate(names):
            diction[heights[i]] = x
        l = 0
        while l < len(names):
            for i in range(len(names)-(l+1)):
                if heights[i] < heights[i+1]:
                    heights[i],heights[i+1] = heights[i+1],heights[i]
            l+=1
        for i in range(len(names)):
            names[i] = diction[heights[i]]
        return names