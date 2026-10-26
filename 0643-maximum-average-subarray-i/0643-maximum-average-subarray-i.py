class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxSum = currentSum = sum(nums[:k])
        for i in range(k, len(nums)): currentSum += nums[i]; currentSum -= nums[i - k]; maxSum = maxSum if maxSum>currentSum else currentSum
        return float(maxSum / k)