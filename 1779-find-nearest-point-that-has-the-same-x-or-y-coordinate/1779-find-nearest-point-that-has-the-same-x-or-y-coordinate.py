class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = []
        dict = {}
        distance = float('inf')
        for i,j in points:
            if i == x or j == y:
                valid.append([i,j])
        for i,j in valid:
            distance = min(distance,(abs(x-i) + abs(y-j)))
            if distance in dict:
                continue
            dict[distance] = points.index([i,j])
        
        if dict:
            return dict[distance]
        else:
            return -1