class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = maxA = 0; right = len(height)-1
        while left < right:
            maxA = max((min(height[right], height[left]) * (right - left)), maxA)
            if height[left] < height[right]: left+=1
            else: right-=1
        return maxA