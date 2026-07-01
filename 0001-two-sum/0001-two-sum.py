class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # We will be storing the hashmap key value pairs like values as key and index as value pair -> {value: index}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[number] = index
            