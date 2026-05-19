class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if (nums1[0] > nums2[-1]) or (nums2[0] > nums1[-1]):
            return -1

        min_len = min(len(nums1), len(nums2))
        num1_pointer = 0
        num2_pointer = 0
        while (num1_pointer < len(nums1)) and (num2_pointer < len(nums2)):
            if nums1[num1_pointer] == nums2[num2_pointer]:
                return nums2[num2_pointer]
            elif nums1[num1_pointer] > nums2[num2_pointer]:
                num2_pointer += 1
            else:
                num1_pointer += 1

        return -1


        