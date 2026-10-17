class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            curr = num
            digit_sum = 0
            while curr:
                digit_sum += curr % 10
                curr //= 10
            nums[i] = (digit_sum, num, i)
        nums.sort()
        nums = [num[2] for num in nums]
        n = len(nums)
        visited = [False] * n
        cycle = 0

        for i, num in enumerate(nums):
            if visited[i]:
                continue
            
            cycle += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = nums[j]
        print(n, cycle)
            
        return n - cycle
        