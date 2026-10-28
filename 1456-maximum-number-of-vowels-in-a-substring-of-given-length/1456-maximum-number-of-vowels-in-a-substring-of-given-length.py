class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        vowels = set('aeiou')
        max_num_vowels = num_vowels = sum(s.count(v, 0, k) for v in vowels)
        #max_num_vowels = num_vowels = sum([1 for c in s[:k] if c in vowels])
        for new_c, gone_c in zip(s[k:], s):
            if new_c in vowels:
                num_vowels += 1
            if gone_c in vowels:
                num_vowels -= 1
            if max_num_vowels < num_vowels:
                max_num_vowels = num_vowels
                if max_num_vowels == k:
                    break
        return max_num_vowels