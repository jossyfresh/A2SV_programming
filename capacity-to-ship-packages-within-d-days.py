class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        SSum = sum(weights)
        def possible(cap):
            count = 0
            Sum = 0
            i = 0
            while i < len(weights):
                if weights[i] > cap:
                    return False
                if Sum + weights[i] > cap:
                    count += 1
                    Sum = 0
                Sum += weights[i]
                i += 1
            count +=1
            if count <= days:
                return True
            return False
        l = -1
        r = SSum
        while r-l > 1:
            mid = (l+r)//2
            if possible(mid):
                r = mid
            else:
                l = mid
        return r