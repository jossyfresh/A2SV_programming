class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        nums = list(zip(nums1,nums2))
        def split(l,r,nums):
            if l >= r:
                return [nums[l]]
            mid = (l+r)//2
            left = split(l,mid,nums)
            right = split(mid+1,r,nums)
            return merge(left,right)
        def merge(left,right):
            nonlocal ans
            i = 0
            j = 0
            while i < len(left):
                while j < len(right) and left[i][0] - right[j][0] <= left[i][1] - right[j][1] + diff:
                    j+=1
                ans+=j
                i+=1
            l = 0
            r = 0
            new = []
            while l < len(left) and r < len(right):
                if left[l][0] - left[l][1] > right[r][0] - right[r][1]:
                    new.append(left[l])
                    l+=1
                else:
                    new.append(right[r])
                    r+=1
            while l < len(left):
                new.append(left[l])
                l+=1
            while r < len(right):
                new.append(right[r])
                r+=1
            return new
        print(split(0,len(nums)-1,nums))
        return ans