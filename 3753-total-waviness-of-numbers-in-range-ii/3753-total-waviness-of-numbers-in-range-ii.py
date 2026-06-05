@cache
def iswav(num: int) -> bool:
    a, b, c = num // 100, num % 100 // 10, num % 10
    return (a < b and c < b) or (a > b and c > b)


wvsub2d = [i for i in range(99) if iswav(i)]
wvsub3d = [i for i in range(101,990) if iswav(i)]


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def helper(num: int) -> int:
            if num < 101:
                return 0
            res = 0
            s = str(num)
            n = len(s)
            for i in range(1, n - 1):
                pfx = int(s[: i - 1]) if i > 1 else 0
                sfx = int(s[i + 2 :]) if i < n - 2 else 0
                mid = int(s[i - 1 : i + 2])
                ls = 10 ** (n - i - 2)
                for j in wvsub2d:
                    if i == 1:
                        break
                    #Be careful of leading zeroes!
                    if j < mid:
                        res += pfx * ls
                    elif j == mid:
                        res += (pfx - 1) * ls + sfx + 1
                    else:
                        res += (pfx - 1) * ls
                for j in wvsub3d:
                    if j < mid:
                        res += (pfx + 1) * ls
                    elif j == mid:
                        res += pfx * ls + sfx + 1
                    else:
                        res += pfx * ls
                # print(res)
            return res

        return helper(num2) - helper(num1 - 1)