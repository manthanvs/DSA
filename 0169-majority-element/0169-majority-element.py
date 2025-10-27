class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using the Moore's voting algorithm here to effectively use the O(1) complexity. 
        votes = 0
        candidate = None

        for n in nums:
            # here n will iterate with every nums and carry out one value each at a time.

            # Here we would check if votes for current candidate is 0, 
            if votes == 0:
                # suppose if this is first iteration, then automatically we will select that particular candidate. 
                # suppose if this is not the first iteration, and it's votes are equal then we would elect the next candidate. i.e. candidate = (n <- current candidate) 
                candidate = n

            # Using the Python ternary conditional expression/one-line if-else: 
            # value_if_true if condition else value_if_false
            votes = votes + (1 if n == candidate else -1)

        return candidate