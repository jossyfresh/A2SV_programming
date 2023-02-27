class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        l = -1
        for indx,val in enumerate(arr):
            while stack and stack[-1][0] > val:
                new = stack.pop()
                if len(stack) == 0:
                    ans+= new[0]*((new[1]-l)* (indx - new[1]))
                else:
                    ans+= new[0] * (new[1] - stack[-1][1]) * (indx - new[1])
            stack.append([val,indx])
        r = indx+1
        print(ans)
        print(stack)
        while stack:
            new = stack.pop()
            if len(stack) == 0:
                ans+= new[0] * (new[1]-l) * (r - new[1])
            else:
                ans+= new[0] * (new[1] - stack[-1][1]) * (r - new[1])
        return ans%((10**9)+7)