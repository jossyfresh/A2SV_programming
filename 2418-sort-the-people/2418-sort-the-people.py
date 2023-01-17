class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = heights.copy()
        x.sort()
        x.reverse()
        print(x)
        print(heights)
        l = 0
        while l < len(names):
            if x != heights:
                for i in range(len(names)-(l+1)):
                    if heights[i] < heights[i+1]:
                        heights[i],heights[i+1] = heights[i+1],heights[i]
                        names[i],names[i+1] = names[i+1],names[i]
            else:
                break
            l+=1
        return names