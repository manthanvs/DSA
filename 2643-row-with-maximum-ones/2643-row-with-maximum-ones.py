class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        hashmap = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    hashmap[i] = hashmap.get(i, 0) + 1

        if not hashmap:
            return [0, 0]

        row = max(hashmap, key=hashmap.get)
        return [row, hashmap[row]]