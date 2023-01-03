class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        colCounter = Counter(zip(*grid))
        return sum(colCounter[row] for row in map(tuple, grid))