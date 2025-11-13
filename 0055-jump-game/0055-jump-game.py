class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        # using one line if else statement => which is, (perform stmt) if [condition is true] else (perform this stmt)  
        return True if goal == 0 else False
