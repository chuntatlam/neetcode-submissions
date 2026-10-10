class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        h = set()
        h.add(s[0])
        l, r = 0, 1
        max_length = 0
        while r < len(s):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            length = r - l + 1
            max_length = max(max_length, length)
            h.add(s[r])
            r += 1
        return max_length

