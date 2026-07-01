class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # TO solve from the last index of the nums1 where every element is zero.
        pointer_for_num1 = m - 1
        pointer_for_num2 = n - 1
        # Hence make a use of the tail. 
        tail = m + n - 1

        while pointer_for_num1 >= 0 and pointer_for_num2 >= 0:
            if nums2[pointer_for_num2] >= nums1[pointer_for_num1]:
                nums1[tail] = nums2[pointer_for_num2]
                pointer_for_num2 -= 1
            else:
                nums1[tail] = nums1[pointer_for_num1]
                pointer_for_num1 -= 1
            tail -= 1
        
        # For Conditions when: nums1 = [4,5,6,0,0,0] and num2 = [1,2,3]

        while pointer_for_num2 >= 0:
            nums1[tail] = nums2[pointer_for_num2]
            pointer_for_num2 -= 1
            tail -= 1