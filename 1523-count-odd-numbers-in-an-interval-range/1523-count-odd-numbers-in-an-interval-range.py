class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high%2!=0 or low%2!=0:
            return (high-low)//2+1
        else:
            return (high-low)//2