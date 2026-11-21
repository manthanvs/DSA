class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        d0 = d1 = ans = 1
        for a, b in pairwise(nums):
            match b - a:
                case 0:
                    d1 = d0 + 1
                case 1:
                    d0 += 1
                    d1 += 1
                case 2:
                    d0, d1 = d1 + 1, 1
                case _:
                    d0 = d1 = 1
            if d0 > ans: ans = d0
            if d1 > ans: ans = d1
        return ans