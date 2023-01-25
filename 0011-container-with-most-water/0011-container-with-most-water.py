class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest = 0
        x,r = 0,len(height)-1
        while x < r:
            area = min(height[x],height[r]) * (r-x)
            if area > highest:
                highest = area
            if height[r] < height[x]:
                r = r-1
            else:
                x+=1
        return highest