class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        seen = set()

        running_sum = 0
        previous_remainder = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            # Check first. The set only contains remainders
            # far enough behind to produce length >= 2.
            if remainder in seen:
                return True

            # Make the previous prefix available for
            # the next iteration.
            seen.add(previous_remainder)
            previous_remainder = remainder

        return False