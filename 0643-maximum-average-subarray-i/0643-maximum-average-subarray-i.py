class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxSum = currentSum = sum(nums[:k])
        for i in range(k, len(nums)): currentSum += nums[i]; currentSum -= nums[i - k]; maxSum = max(currentSum, maxSum)
        return float(maxSum / k)