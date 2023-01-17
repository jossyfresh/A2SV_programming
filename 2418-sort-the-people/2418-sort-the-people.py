class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        k = 0
        for j in range(len(names)):
            largest = heights[j]
            k = j
            for i in range(j+1,len(names)):
                if largest < heights[i]:
                    largest = heights[i]
                    k = i  
            heights[j],heights[k] = heights[k],heights[j]
            names[j],names[k] = names[k],names[j]
                    
        return names