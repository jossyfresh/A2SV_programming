class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        k = 3
        i = 0
        if len(nums) <= 3:
            return 0
        else:
            queue = deque(nums)
            l = 3
            while k > 0:
                if abs(queue[-k-1] - queue[0]) > abs(queue[k]-queue[-1]): 
                    queue.popleft()
                else:
                    queue.pop()
                k -= 1
        return queue[-1] - queue[0]