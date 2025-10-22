class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Creating a left pointer which will point the unique value in the nums[]
        # Since the first value is always unique we proceed to check futher. 
        left = 1
        
        for i in range(1, len(nums)):
            # Since this is an non-descreasing order, we have to check the current value with the previous value i.e. - 1 index to check if it is same or unique 
            if nums[i] != nums[i-1]:
                # If they aren't same, i.e. unique then we dump the new value(nums[i]) onto the left pointer [nunms[left]]
                nums[left] = nums[i]
                # Since the unique value is pasted we can proceed to increament the unique value.
                left += 1
            # Since we have the number of unique elements we can go ahead and return the left.
        return left