class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def checkList(left, right):
            nonlocal res, resLen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            # odd length
            checkList(i, i)
            # even length
            checkList(i, i + 1)
        return res
