class Solution {
    public boolean isPalindrome(String s) {
        String valid_s = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");
        for (int left = 0, right = valid_s.length() - 1; left < right; left++, right--) {
            if (valid_s.charAt(left) != valid_s.charAt(right)) {
                return false;
            }
        }
        return true;
    }
}