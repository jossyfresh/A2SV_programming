class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1,len(names)):
            key = heights[i]
            word = names[i]
            j = i-1
            while j >= 0 and heights[j] < key:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j-=1
            names[j+1] = word
            heights[j+1] = key

                
                      
        return names