class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(num,target):
            if (tuple(num),target) in memo:
                return memo[(num,target)]
            if len(num) == 0 and target == 0:
                return 1
            if len(num) == 0 and target != 0:
                return 0
            val = dfs(tuple(num[1:]),target-num[0]) + dfs(tuple(num[1:]),target+num[0])
            memo[(tuple(num),target)] = val
            return val
        return dfs(tuple(nums),target)