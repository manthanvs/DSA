class Solution:
    def maxBuilding(self, num: int, r: list[list[int]]) -> int:
        def yCap(l, b):
            x1, y1 = l
            x2, y2 = b
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(l, b):
            x1, y1 = l
            x2, y2 = b
            return (y1 + y2 + x2 - x1) // 2

        r.append([1, 0])
        r.sort()
        n = len(r)

        for i in range(1, n):
            r[i][1] = yCap(r[i - 1], r[i])

        for i in range(n - 2, -1, -1):
            r[i][1] = yCap(r[i + 1], r[i])

        res = 0
        for i in range(1, n):
            res = max(res, yPeak(r[i - 1], r[i]))

        return max(res, r[-1][1] + num - r[-1][0])