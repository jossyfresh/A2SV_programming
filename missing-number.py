class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct_position = arr[i]
            if correct_position < len(arr)-1 and arr[correct_position] != arr[i]:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]
            else:
                i += 1
        l = 0
        for x in arr:
            if x == l:
                l+=1
            else:
                return l
        return l