import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int ans[] = new int[nums.length];
        int ProdL = 1;
        int ProdR = 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            ans[i] = ProdR;
            ProdR = ProdR * nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            ans[i] = ans[i] * ProdL;
            ProdL = ProdL * nums[i];

        }
        return ans;
    }
}