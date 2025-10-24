class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        # We’re allowed to keep each number at most twice.
        # For example: [1,1,2,2,3,3] is valid,
        # but [1,1,1,2,2,3,3,3] is not (because 1 and 3 appear three times).

        # We'll use two pointers:
        # - "read" goes through every element in the list.
        # - "write" marks where the next valid number should be written.
        # This lets us modify the list in place without creating a new one.
        
        write = 0
        
        # The loop moves the "read" pointer across the list.
        for read in range(len(nums)):
            # For each [read]:
            # 1. If we’ve written fewer than two numbers so far (write < 2), we always keep the current one.
            # 2. Otherwise, we compare the current value to the one two spots back [write - 2]. If they’re different, it means this is a new number or only the second duplicate — so we keep it.
                
            if write < 2 or nums[read] != nums[write - 2]:
                # If the condition is true, this value is allowed.
                # Copy it into the write position and move write forward.
                nums[write] = nums[read]
                write += 1

            # If the condition is false, it means this is the third (or later) occurrence of the same number — so we skip it.
            
        # "write" is now equal to the length of the valid portion(only two pair of duplicates not more than that) of the array.
        return write
