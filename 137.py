class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = {}
        for x in nums:
            if x in maps:
                maps[x] = maps.get(x,0) + 1
            else:
                maps[x] = 1
        for x in nums:
            if maps[x] == 1:
                return x
        