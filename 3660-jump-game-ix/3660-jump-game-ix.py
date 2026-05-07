class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [nums[0]] # prefix
        for i in range(1, N):
            ans.append(max(ans[-1], nums[i]))

        min_idx = N - 1
        for i in range(N - 2, -1, -1):
            if ans[i] > nums[min_idx]:
                ans[i] = ans[min_idx]
            if nums[i] < nums[min_idx]:
                min_idx = i
        return ans