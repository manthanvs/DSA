class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for s in strs:
            sorted_array = "".join(sorted(s))
            # if there are an sorted_array key in the hashtable with the sorted array:
            # eg: eat=> aet as index.
            if sorted_array in hashtable:
                hashtable[sorted_array].append(s)
            else:
                # Instead of the string "s" we would store them in a list. So that we could use the append methods as well.
                hashtable[sorted_array] = [s]
        return list(hashtable.values())
