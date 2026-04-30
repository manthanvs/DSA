class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        if s == 0:
            return 0
        if s == n:
            return s - 1
        prev = 0
        curr = 0
        res = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                res = max(res, prev + curr)
                prev = curr
                curr = 0
        res = max(res, prev + curr)
        return res