class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        l =0 
        r = len(y)-1
        while l<r:
            if y[l] == y[r]:
                l+=1
                r-=1
            else:
                return False
        return True