class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        max_ones = 0
        row_index = 0

        for i in range(len(mat)):
            ones = sum(mat[i])

            if ones > max_ones:
                max_ones = ones
                row_index = i

        return [row_index, max_ones]