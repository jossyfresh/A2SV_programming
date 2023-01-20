class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1,n2):
            n = min(len(n1),len(n2))
            for i in range(n):
                if n1[i] > n2[i]:
                    return n2
                elif n1[i] < n2[i]:
                    return n1
            new1 = n1+n2
            new2 = n2+n1
            if new1 > new2:
                return n2
            else:
                return n1
        for i in range(len(nums)):
            nums[i] = str(nums[i])
      
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if compare(nums[j],nums[j+1]) == nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
       
        ans = ""
        for k in range(len(nums)-1,-1,-1):
            ans+=nums[k]
        ans = int(ans)
        return str(ans)
 