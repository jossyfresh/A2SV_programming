class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        nums = list(enumerate(nums))
        def split(l,r,nums):
            if l >= r:
                return [nums[l]]
            mid = (l+r)//2
            left = split(l,mid,nums)
            right = split(mid+1,r,nums)
            return merge(left,right)
        def merge(left,right):
            l = 0
            r = 0
            new = []
            count = 0
            while l < len(left) and r < len(right):
                if left[l][1] > right[r][1]:
                    new.append(right[r])
                    count += 1
                    r+=1
                else:
                    new.append(left[l])
                    ans[left[l][0]] += count
                    l+=1
            while l < len(left):
                new.append(left[l])
                ans[left[l][0]] += count
                l+=1
            while r < len(right):
                new.append(right[r])
                r+=1
            return new
        split(0,len(nums)-1,nums)
        return ans