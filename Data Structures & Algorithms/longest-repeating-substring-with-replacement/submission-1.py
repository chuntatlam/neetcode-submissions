class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        for c in charSet:
            l, r = 0, 0
            for i in range(len(s)):
                if s[i] != c:
                    continue
                count = 1
                replacement = 0
                while i < len(s) and replacement < k:
                    if s[i] != c:
                        replacement += 1
                    count += 1
                    res = max(res, count)
                    i += 1
        return res
