class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Because K can be greater than the lenght of the array. and the logic for 
        # k = k % len(nums) is that the values of the k would never exceed the len(nums)
        # i.e. k= 7 and len(nums)=4 then k = 7 % 5 = 2 which is rotated back from the start.
        k %= len(nums)
        
        
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l = k
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
