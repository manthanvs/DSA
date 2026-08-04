class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxNums, minNums = max(nums), min(nums)
        list = []

        for i in range(minNums, maxNums):
            if i+1 not in nums:
                list.append(i+1)
        return list