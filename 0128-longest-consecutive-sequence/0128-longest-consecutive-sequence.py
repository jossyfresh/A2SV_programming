class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            ans = 0
            count = 0
            nums.sort()
            print(nums)
            for x in nums:
                first = x
                break
            print(first)
            for i in nums:
                if i == first:
                    continue
                elif i == first+1:
                    count+=1
                    first = i
                elif i != first+1:
                    ans = max(ans,count+1)
                    count = 0
                    first = i
            ans = max(ans,count+1)
            return ans
        return 0
