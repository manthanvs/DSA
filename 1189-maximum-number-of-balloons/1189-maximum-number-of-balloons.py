class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash={}
        for ch in text:
            if ch in "ballon":
                hash[ch]=hash.get(ch,0)+1
        req={"b":1,"a":1,"l":2,"o":2,"n":1}
        result=float("inf")
        for letter , need in req.items():
            have=hash.get(letter,0)
            result=min(result,have//need)
        return result