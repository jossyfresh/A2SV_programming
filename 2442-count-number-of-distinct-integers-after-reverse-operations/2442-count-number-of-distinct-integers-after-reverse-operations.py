class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numbers = set(nums)
        count = len(nums)
        def reverse(num):
            number = []
            i = 0
            val = 0
            while num > 0:
                x = num%10
                num = num//10
                number.append(x)
                i+=1
            for j in number:
                val += j*(10**(i-1))
                i-=1
            return val
        for val in numbers:
            nums.append(reverse(val))
        nums = set(nums)
    
        return len(nums)
    
    