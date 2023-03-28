class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct_position = arr[i] - 1
            if correct_position < len(arr) and correct_position >= 0 and arr[correct_position] != arr[i]:
                arr[correct_position], arr[i] = arr[i], arr[correct_position]
            else:
                i += 1
        n = 1
        for x in arr:
            if x == n:
                n+=1
            else:
                return n
        return n