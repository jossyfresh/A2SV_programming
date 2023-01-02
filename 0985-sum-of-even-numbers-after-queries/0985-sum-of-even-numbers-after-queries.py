class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prevsum = 0
        dict = {}
        for i,x in enumerate(nums):
            if x%2 == 0:
                prevsum += x
                dict[i] = x
            else:
                continue
        ans = []
        for val, i in queries:
            nums[i]+=val
            if nums[i]%2 == 0:
                if i in dict:
                    prevsum+=val
                    dict[i] = nums[i]
                    ans.append(prevsum)
                else:
                    prevsum+=nums[i]
                    dict[i] = nums[i]
                    ans.append(prevsum)
            else:
                if i in dict:
                    prevsum -= dict[i]
                    dict.pop(i)
                    ans.append(prevsum)
                else:
                    ans.append(prevsum)
        return ans
