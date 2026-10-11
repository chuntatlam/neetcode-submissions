class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # use Counter object
        ct = collections.Counter(t)

        l = 0
        cs = collections.Counter()
        shortest_sub = ""
        for r in range(len(s)):
            # check condition (if all char in t is in window)
            cs[s[r]] += 1
            while ct <= cs:
                curr_sub_l = r - l + 1
                # compare length of curr_sub and shortest_sub
                if len(shortest_sub) == 0:
                    shortest_sub = s[l:r+1]
                if curr_sub_l < len(shortest_sub):
                    shortest_sub = s[l:r+1]
                # increase l to make window smaller
                cs[s[l]] -= 1
                l += 1
        return shortest_sub
