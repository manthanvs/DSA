class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Creating a unique_index pointer which will point the unique value in the nums[]
        # Since the first value is always unique we proceed to check futher. 
        unique_index = 1
        
        for i in range(1, len(nums)):
            # Since this is an non-descreasing order, we have to check the current value with the previous value i.e. - 1 index to check if it is same or unique 
            if nums[i] != nums[i-1]:
                # If they aren't same, i.e. unique then we dump the new value(nums[i]) onto the left pointer [nunms[left]]
                nums[unique_index] = nums[i]
                # Since the unique value is pasted we can proceed to increament the unique value.
                unique_index += 1
            # Since we have the number of unique elements we can go ahead and return the left.
        return unique_index