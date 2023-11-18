class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for x in count:
            if count[x] > (len(nums) // 3):
                ans.append(x)
        return ans