class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        current = longest = 0

        for i in hashset:
            if i - 1 not in hashset:
                current = i
                length = 1
                # Which means we found the first domino tile.
                while current + 1 in hashset:
                    current += 1
                    length += 1
                    # We iterate till the last domino tile falls.
                longest = max(longest, length)
                # Compare which Domino set was bigger. then return the longest set of domino tiles.
        return longest
