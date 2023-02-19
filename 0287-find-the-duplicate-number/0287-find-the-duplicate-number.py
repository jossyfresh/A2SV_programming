class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            if x in dict:
                return x
            dict[x] = 1