class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current = 0
        vowels = 'aeiou'
        for i in range(k): 
            if s[i] in vowels: current += 1
        maxVowels = current
        for i in range(k, len(s)):
            if s[i-k] in vowels: current -= 1
            if s[i] in vowels:
                current += 1
                if current > maxVowels: maxVowels = current
        return maxVowels