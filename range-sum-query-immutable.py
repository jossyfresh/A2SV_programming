class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0]
        Sum = 0
        for x in self.nums:
            Sum+=x
            prefix.append(Sum)
        return prefix[right+1] -prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)