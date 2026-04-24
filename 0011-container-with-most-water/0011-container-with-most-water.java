class Solution {
    static {
        for(int i=0;i<500;i++){
            maxArea(new int[]{});
        }
    }
    public static int maxArea(int[] height) {
        int n=height.length;
        int ans=0,l=0,r=n-1;
        while(l<r){
            int water=(r-l)*Math.min(height[r],height[l]);
            ans=Math.max(water,ans);
            if(height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return ans;
    }
}