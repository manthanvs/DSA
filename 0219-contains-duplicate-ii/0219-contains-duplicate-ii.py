class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        nums.reverse() 
        for left in range(len(nums) - 1):
            for right in range(left + 1, min(left + k+1, len(nums))):

                if nums[left] == nums[right]:
                    return True
        return False