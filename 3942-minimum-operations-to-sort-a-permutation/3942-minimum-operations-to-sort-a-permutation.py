class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x=nums.index(0)
        n=len(nums)
        if n<3:return 1 if x else 0
        v1,v2=nums[(x+1)%n],nums[(x-1)%n]
        if {v1,v2}=={1,n-1}:
            st=sorted(nums)
            if v1==1 and nums[x:]+nums[:x]==st:
                return min(x,n-x+2)
            elif v2==1 and nums[x+1:]+nums[:x+1]==st[::-1]:
                return min(x+2,n-x)
        return -1
        