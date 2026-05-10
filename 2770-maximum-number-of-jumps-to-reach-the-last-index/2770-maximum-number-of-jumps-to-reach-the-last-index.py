class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mjumps = [-1] * n
        mjumps[n - 1] = 0

        for i in range(n - 2, -1, -1):
            maxj = 0
            for j in range(i + 1, n):
                if mjumps[j] >= maxj and -target <= nums[j] - nums[i] <= target:
                    maxj = mjumps[j]
                    mjumps[i] = maxj + 1
        
        return mjumps[0] if mjumps[0] != 0 else -1
        