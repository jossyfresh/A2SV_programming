class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passangers = [0]*1001
        for x in trips:
            passangers[x[1]] += x[0]
            passangers[x[2]] -= x[0]
        Sum = 0
        for i in range(len(passangers)):
            Sum += passangers[i]
            passangers[i] = Sum
            if passangers[i] > capacity:
                return False
        return True