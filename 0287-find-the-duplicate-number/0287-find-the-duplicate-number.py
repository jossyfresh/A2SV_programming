class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets = set()
        for x in nums:
            if x in sets:
                return x
            sets.add(x)