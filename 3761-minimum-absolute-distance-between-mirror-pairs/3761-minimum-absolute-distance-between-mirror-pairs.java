class Solution {
    public int minMirrorPairDistance(int[] nums) {
        int n = nums.length;
        int ans = n;
        Map<Integer, Integer> lastIdx = new HashMap<>();
        for (int j = 0; j < n; j++) {
            int x = nums[j];
            Integer i = lastIdx.get(x);
            if (i != null) {
                ans = Math.min(ans, j - i);
            }

            int rev = 0;
            for (; x > 0; x /= 10) {
                rev = rev * 10 + x % 10;
            }
            lastIdx.put(rev, j);
        }
        return ans < n ? ans : -1;
    }
}