class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = []
        current_max = -inf

        for i in nums:
            current_max = max(current_max, i)
            mx.append(current_max)

        prefixGcd = [gcd(x, y) for x, y in zip(nums, mx)]
        prefixGcd.sort()

        left, total, right = 0, 0, len(nums) - 1
        while left < right:
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return total
