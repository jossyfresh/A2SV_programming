class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        ans = []
        for x in nums:
            Sum+=x
            ans.append(Sum)
        return ans