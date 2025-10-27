class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using the Moore's voting algorithm here to effectively use the O(1) complexity. 
        votes = 0
        candidate = None

        for num in nums:
            if votes == 0:
                candidate = num

            # Using the Python ternary conditional expression/one-line if-else: 
            # value_if_true if condition else value_if_false
            votes = votes + (1 if num == candidate else -1)

        return candidate