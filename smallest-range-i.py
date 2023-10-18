class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a = min(nums)
        b = max(nums)
        return max(((b-k )- (a+k)),0)