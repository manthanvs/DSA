import java.util.*;  // Imports for Set and HashSet

class Solution {
    public boolean containsDuplicate(int[] nums) {

        // Creates a HashSet to store unique integers (HashSet does not allow duplicates)
        Set<Integer> set = new HashSet<>();  

        // Iterates through each element 'n' in the input array 'nums'
        for (int n : nums) {  
            if (!set.add(n)) 
                return true;  
            // Attempts to add the current number to the set
            // The add() method returns false if the element already exists in the set and If add() returns false, it means a duplicate is found, so return true immediately
        }
        return false;  
        // If the loop completes without finding duplicates, return false. This means all elements in the array are unique
    }
}
