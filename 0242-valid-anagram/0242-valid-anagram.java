class Solution {

    public boolean isAnagram(String s, String t) {

        // If the lengths are different, they cannot be anagrams
        if (s.length() != t.length()) return false;

        // Create an integer array of size 26 to store character frequency
        // Each index represents a lowercase letter from 'a' to 'z'
        int array[] = new int[26];

        // Traverse both strings simultaneously
        for (int i = 0; i < s.length(); i++) {

            // Increment the count for the character in string s
            // (char - 'a') gives index from 0 to 25
            array[s.charAt(i) - 'a']++;

            // Decrement the count for the character in string t
            array[t.charAt(i) - 'a']--;
        }

        // If s and t are anagrams, all values in the array should be 0
        // because increments and decrements cancel each other out
        for (int n : array) {

            // If any value is not zero, characters do not match
            if (n != 0) {
                return false;
            }
        }

        // If all values are zero, strings are valid anagrams
        return true;
    }
}
