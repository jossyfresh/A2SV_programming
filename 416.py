class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum//2
        print(target)
        n = len(nums)
        prev = [False] * (target + 1)
        curr = [False] * (target + 1)
        if nums[0] <= target:
            prev[nums[0]] = True

        prev[0] = curr[0] = True

        print(prev)

        for i in range(1, n):
            for j in range(1, target+1):
                nottake = prev[j]
                take = False
                if nums[i] <= j:
                    take = prev[j - nums[i]]
            
                curr[j] = take or nottake

            prev = curr.copy()
    
        return prev[target]