class Solution:
    from bisect import bisect_left, insort
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n): prefix[i + 1] = prefix[i] + nums[i]
        window = []
        ans = float('inf')
        for i in range(l, n + 1):
            insort(window, prefix[i - l])
            if i - r - 1 >= 0: value = prefix[i - r - 1]; pos = bisect_left(window, value); window.pop(pos)
            pos = bisect_left(window, prefix[i])
            if pos > 0:
                candidate = prefix[i] - window[pos - 1]
                if candidate > 0: ans = min(ans, candidate)
        return -1 if ans == float('inf') else ans