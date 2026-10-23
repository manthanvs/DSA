class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = water = 0; right = len(height)-1
        while left < right:
            water = max((min(height[right], height[left]) * (right - left)), water)
            if height[left] < height[right]: left+=1
            else: right-=1
        return water