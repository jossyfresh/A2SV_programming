class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits)-1
        while r >= 0:
            if digits[r]==9:
                if r==0:
                    digits[r] = 0
                    digits.insert(0,1)
                    break
                digits[r] = 0
                r-=1
            else:
                digits[r]+=1
                break
        return digits