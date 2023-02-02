class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        r = len(piles)-2
        count = 0
        max_ = 0
        while r > 0:
            max_+=piles[r]
            count +=1
            r-=2
            if count==len(piles)//3:
                break
        return max_
            
        