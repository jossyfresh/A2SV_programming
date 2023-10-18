class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        zero = defaultdict(int)
        one = defaultdict(int)
        for i in range(len(nums)):
            if i % 2 == 0:
                zero[nums[i]] += 1
            else:
                one[nums[i]] += 1
        zeros = []
        ones = []
        for x in zero:
            zeros.append((x,zero[x]))
        for y in one:
            ones.append((y,one[y]))
        ones.sort(key=lambda x:x[1], reverse= True)
        zeros.sort(key=lambda x:x[1], reverse= True)
        ones.append([-1,0])
        zeros.append([-1,0])
        a = ones[0][0]
        b = zeros[0][0]
        res = len(nums)
        if a == b:
            a = ones[0][0]
            b = zeros[1][0]
            ans = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] != b:
                        ans += 1
                else:
                    if nums[i] != a:
                        ans += 1
            res = min(res,ans)
            b = zeros[0][0]
            a = ones[1][0]
            ans = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] != b:
                        ans += 1
                else:
                    if nums[i] != a:
                        ans += 1
            res = min(res,ans)
        else:
            ans = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    if nums[i] != b:
                        ans += 1
                else:
                    if nums[i] != a:
                        ans += 1
            res = min(res,ans)
        return res