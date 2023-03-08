class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num,m,h):
            Sum = 0
            for x in num:
                Sum+=ceil(x/m)
            if Sum > h:
                return False
            return True
        l = 0
        r = max(piles)
        while r - l > 1:
            mid = l + (r-l)//2
            if check(piles,mid,h):
                r = mid
            else:
                l = mid
        return r