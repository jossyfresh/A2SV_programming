class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]*len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i] < ratings[i-1]:
                ans[i-1] = max(ans[i] + 1,ans[i-1])
        return sum(ans)

             