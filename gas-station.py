class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = list(zip(cost,gas))
        new = []
        for i in range(len(arr)):
            new.append(arr[i][1] - arr[i][0])
        if sum(new) < 0:
            return -1
        j = 0
        total = 0
        for i in range(len(new)):
            total += new[i]
            if total < 0:
                total = 0
                j = i + 1
        return j