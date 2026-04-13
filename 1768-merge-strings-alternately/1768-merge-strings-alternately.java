class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n=word1.length();
        int m=word2.length();
        char ans[] = new char[n+m];
        int i=0,j=0,k=0;
        while(i<n&&j<m){
            ans[k++] = word1.charAt(i++);
            ans[k++] = word2.charAt(j++);
        }

        while(i<n){
            ans[k++]=word1.charAt(i);
            i++;
        }

        while(j<m){
            ans[k++]=word2.charAt(j);
            j++;
        }

        return new String(ans);
    }
}