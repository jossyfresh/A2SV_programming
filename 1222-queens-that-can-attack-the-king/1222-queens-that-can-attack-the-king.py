class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        i = king[0]
        j = king[1]
        while i >= 0 and j >= 0:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i-=1
            j-=1
        i = king[0]
        j = king[1]
        while i < 8 and j < 8:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i+=1
            j+=1
        i = king[0]
        j = king[1]
        while i < 8 and j >= 0:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i+=1
            j-=1
        i = king[0]
        j = king[1]
        while i >= 0 and j < 8:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i-=1
            j+=1
        i = king[0]
        j = king[1]
        while i < 8:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i+=1
        i = king[0]
        j = king[1]
        while i >= 0:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            i-=1
        i = king[0]
        j = king[1]
        while j < 8:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            j+=1
        i = king[0]
        j = king[1]
        while j >= 0:
            x = [i,j]
            if x in queens:
                ans.append(x)
                break
            j-=1
        return ans
        
                
            
        