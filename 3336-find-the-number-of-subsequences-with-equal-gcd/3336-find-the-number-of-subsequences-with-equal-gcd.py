from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[(g1, g2)] stores the number of disjoint subsequence pairs 
        # with GCDs g1 and g2 respectively.
        dp = {(0, 0): 1}
        
        for num in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Option 1: Put num into the first subsequence
                ng1 = gcd(g1, num)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                # Option 2: Put num into the second subsequence
                ng2 = gcd(g2, num)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans