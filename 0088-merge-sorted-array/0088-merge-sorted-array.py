class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 'nums1' has extra space at the end to hold all elements after merging.
        # Example: nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]
        # m = number of valid elements in nums1
        # n = number of valid elements in nums2

        # Index of the last position in nums1 where we’ll place the next largest element
        last = m + n - 1

        # We will compare elements from the end of nums1 and nums2
        # and fill nums1 from the back (to avoid overwriting existing elements)
        while m > 0 and n > 0:
            # Compare the last valid elements of both arrays
            if nums1[m - 1] > nums2[n - 1]:
                # If nums1’s element is larger, put it at the end (nums1[last])
                nums1[last] = nums1[m - 1]
                # Move nums1 pointer one step left
                m -= 1
            else:
                # If nums2’s element is larger (or equal), put it at the end
                nums1[last] = nums2[n - 1]
                # Move nums2 pointer one step left
                n -= 1

            # Move the 'last' pointer left for the next position
            last -= 1

        # If any elements are still left in nums2 (nums1's remaining are already sorted),
        # copy them over to nums1.
        # This happens when nums2 has smaller numbers that should go at the start.
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1