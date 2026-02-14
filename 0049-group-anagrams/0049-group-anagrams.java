class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        // Map to store grouped anagrams
        // Key   -> frequency representation of characters
        // Value -> list of strings having same character frequency
        HashMap<String, List<String>> map = new HashMap<>();
        
        // Final result list containing all grouped anagrams
        List<List<String>> res = new ArrayList<>();

        // Iterate through each string in input array
        for(String str : strs) {
            
            // Create a frequency array for 26 lowercase letters (a–z)
            char[] num = new char[26];
            
            // Convert current string into character array
            char[] ch = str.toCharArray();
            
            // Count frequency of each character
            for(char c : ch) {
                num[c - 'a']++;   // Increment index based on character position
            }
            
            // Convert frequency array into a String
            // This acts as a unique key for anagrams
            String sb = new String(num);
            
            // If key already exists, add string to existing list
            if(map.containsKey(sb)){
                map.get(sb).add(str);
            } 
            else {
                // Otherwise create a new list for this anagram group
                ArrayList<String> list = new ArrayList<>();
                list.add(str);
                
                // Store new group in map
                map.put(sb,list);
                
                // Also add this list to final result
                res.add(list);
            }
        }
        
        // Return grouped anagrams
        return res;
    }
}

// Stack Flow Summary

// For each string:
// Create frequency array
// → Build unique key
// → Check if key exists in map
//     → YES → add to existing list
//     → NO  → create new list, store in map and res
