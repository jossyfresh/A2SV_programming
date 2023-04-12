class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        min_ = 0 
        for x in count:
            min_ = math.gcd(count[x],min_)
        if min_ <= 1:
            return False
        for x in count:
            if count[x] % min_ != 0:
                return False
        return True