class Solution {
    public boolean isSubsequence(String s, String t) {
    int i = 0;
    int j = 0;
    int t_length = t.length();
    int s_length = s.length();
    char chars_s[] = s.toCharArray();
    char chars_t[] = t.toCharArray();

    if(s_length < 1) return true;

    while(i < t_length){
        if(chars_t[i]==chars_s[j]){
            j++;
        }
        i++;
    if(j == s_length) return true;
    }
    return false;
    }
}