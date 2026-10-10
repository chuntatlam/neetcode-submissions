class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        h = {}
        while r < len(s):
            h[s[r]] = 1 + h.get(s[r], 0)
            while (r - l + 1) - max(h.values()) > k:
                h[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
