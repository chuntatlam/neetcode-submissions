class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        charSet = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            length = r - l + 1
            res = max(res, length)
            charSet.add(s[r])
            r += 1
        return res
