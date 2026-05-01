class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_s = sum(nums)
        rolling_sum = 0
        best = 0
        start = 0
        for i in range(n-1,0,-1):
            start += i*nums[i]
            i_change = total_s - n*nums[i]
            rolling_sum = rolling_sum + i_change
            if rolling_sum > best: best = rolling_sum
        return start + best 