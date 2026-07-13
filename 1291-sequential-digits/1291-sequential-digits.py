class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        List = []
        # for numbers that or on the least significant bit.
        queue = deque(range(1, 10))

        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                List.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
        return List
