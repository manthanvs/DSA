class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum = 0
        for i in range(k): currentSum += nums[i]
        maxSum = currentSum
        for i in range(k, len(nums)): currentSum += nums[i]; currentSum -= nums[i - k]; maxSum = max(currentSum, maxSum)
        return float(maxSum / k)