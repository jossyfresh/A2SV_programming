class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a= set()
        for x in nums:
            a.add(x)
        i = 1
        while True:
            if i not in a:
                return i
            i+=1
            