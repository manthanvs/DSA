class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Because K can be greater than the lenght of the array. suppose k is 10 and n is 7, rotating 10 times is the same as rotating 3 times (10 % 7 = 3).
        # This handles cases where k > n and also k=0.
        # Your comment for this part was spot on.
        k %= len(nums)
        
        # If k is zero then we don't need to change anything.
        if k == 0:
            return
        
        # Let's try by reversing three sections of the list. Let's trace with an example:
        
        
        # Let's say that the nums = [1, 2, 3, 4, 5, 6, 7]
        # and given k = 3
        # We want to get: [5, 6, 7, 1, 2, 3, 4]

        # 1st section: Reverse the ENTIRE list
        
        # Considering pointers for the start (l) and end (r) of the list.
        l = 0
        r = len(nums) - 1

        # reverse logic
        # Loop until the left pointer passes the right pointer.
        while l < r:
            # We swap the elements at the left and right pointers.
            nums[l], nums[r] = nums[r], nums[l]
            # Increament left pointer one step.
            # Decreement right pointer one step.
            l, r = l + 1, r - 1
        
        # After Reversal 1, nums is:        
        # [7, 6, 5, 4, 3, 2, 1]


        # Second section: Reverse the FIRST 'k' elements
        
        # Set pointers for the start (l=0) and the (k-1)th element, just because the "l" starts from 0 instead of 1
        l = 0
        r = k - 1
        
        # Loop until the pointers meet, reversing the first k elements.
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        # After Reversal 2, nums is:
        # The first k elements [7, 6, 5] become [5, 6, 7].
        # [5, 6, 7, 4, 3, 2, 1] now we can see that we have kth elements in position. As the actual answer we need is: [(5),(6),(7),1,2,3,4]
        
        
        
        # Third and last sectipn: Reverse the REMAINING 'n-k' elements ---
        
        # Set pointers for the k-th element (l=k) and the end of the list.
        l = k
        r = len(nums) - 1

        # Loop until the pointers meet, reversing the first k elements.
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        # After Reversal 3, nums is:
        # The remaining elements [4, 3, 2, 1] become [1, 2, 3, 4].
        # [5, 6, 7, 1, 2, 3, 4]
        
        # The list 'nums' is now fully rotated in-place with O(1). 