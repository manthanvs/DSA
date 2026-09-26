from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []          # saves previous states
        res = []            # accumulates union results (comma-separated)
        cur = []            # accumulates current concatenation product

        for ch in expression:
            if ch.isalpha():
                # Append the letter to every word in cur (or start with the letter)
                cur = [word + ch for word in cur] or [ch]

            elif ch == '{':
                # Save current state and start fresh inside the braces
                stack.append(res)
                stack.append(cur)
                res, cur = [], []

            elif ch == '}':
                # Restore the previous state and combine with inner result
                prev_cur = stack.pop()
                prev_res = stack.pop()

                # The inner result is res + cur (union of all parts inside the braces)
                inner = res + cur

                # Cartesian product with the saved concatenation context
                if prev_cur:
                    cur = [p + c for p in prev_cur for c in inner]
                else:
                    cur = inner

                res = prev_res

            elif ch == ',':
                # A comma ends the current concatenation part; add it to the union
                res += cur
                cur = []

        # Final result is the union of all comma-separated parts
        result_set = set(res + cur)
        return sorted(result_set)