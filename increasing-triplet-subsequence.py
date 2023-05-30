class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = []
        
        smallest = float('inf')
        middle = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= middle:
                middle = num
            else:
                return True
        return False