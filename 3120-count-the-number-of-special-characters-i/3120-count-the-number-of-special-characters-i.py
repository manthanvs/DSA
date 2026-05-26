class Solution(object):
    def numberOfSpecialChars(self, word):
        smallSet = set()
        capitalSet = set()
        
        for char in word:
            if char >= 'a' and char <= 'z':
                smallSet.add(char)
            else:
                capitalSet.add(char)
        
        count = 0
        for char in smallSet:
            if char.upper() in capitalSet:
                count += 1
        
        return count