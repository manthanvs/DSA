class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Count the first window using built-in string operations.
        count = best = sum(s.count(v, 0, k) for v in "aeiou")

        if best == k or k == len(s):
            return best

        # Convert each character to 1 for a vowel, 0 otherwise.
        table = bytes(1 if c in b"aeiou" else 0 for c in range(256))
        flags = s.encode().translate(table)

        for outgoing, incoming in zip(flags, flags[k:]):
            if incoming:
                if not outgoing:
                    # A vowel replaces a consonant: count increases.
                    count += 1
                    if count > best:
                        best = count
                        if best == k:
                            return k
            elif outgoing:
                # A consonant replaces a vowel: count decreases.
                count -= 1

        return best