class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_one = current_one = 0
        for num in nums:
            if num == 1:
                current_one += 1
                if current_one > max_one: max_one = current_one
            else: current_one = 0
        return max_one