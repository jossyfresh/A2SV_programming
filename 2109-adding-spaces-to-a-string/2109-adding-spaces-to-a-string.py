class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = 0
        i = 0
        new = ""
        while l < len(s):
            if i < len(spaces):
                if l == spaces[i]:
                    new+=" "
                    i+=1
            new+=s[l]
            l+=1
            
        return new
                
            
        