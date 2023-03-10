class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        min_ = float("inf")
        cookies = sorted(cookies)[::-1]
        print(cookies)
        def back(i,buck):
            nonlocal min_
            if i >= len(cookies):
                min_ = min(min_,max(buck))
                return
            if max(buck) > min_:
                return 
            for j in range(k):
                buck[j] += cookies[i]
                back(i+1,buck)
                buck[j] -= cookies[i]

        back(0,bucket)
        return min_