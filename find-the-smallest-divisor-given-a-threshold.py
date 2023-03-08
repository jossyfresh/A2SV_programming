class Solution:
    def smallestDivisor(selExaminef, nums: List[int], threshold: int) -> int:
        def check(nums,n):
            Sum = 0
            for x in nums:
                Sum += ceil(x/n)
            return Sum
        l = 0
        r = 10**6
        while r - l > 1:
            mid = l + (r-l)//2
            if check(nums,mid) <= threshold:
                r = mid
            else:
                l = mid
        return r