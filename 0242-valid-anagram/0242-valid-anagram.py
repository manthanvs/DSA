class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            
        hashtable = {}

        for i in s:
            hashtable[i] = hashtable.get(i, 0) + 1

        for i in t:
            if hashtable.get(i,0)==0:
                return False
            hashtable[i]-=1
        return True