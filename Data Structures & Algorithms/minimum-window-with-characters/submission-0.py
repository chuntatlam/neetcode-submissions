class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # use Counter object
        ct = collections.Counter(t)

        l = 0
        cs = collections.Counter()
        res = ""
        curr_sub = ""
        shortest_sub = ""
        for r in range(len(s)):
            # check condition (if all char in t is in window)
            cs[s[r]] += 1
            while ct <= cs:
                res = s[l:r+1]
                curr_sub = s[l:r+1]
                # compare length of curr_sub and shortest_sub
                if shortest_sub == "":
                    shortest_sub = curr_sub
                elif len(curr_sub) < len(shortest_sub):
                    shortest_sub = curr_sub
                else:
                    pass
                # increase l to make window smaller
                cs[s[l]] -= 1
                l += 1
        print(res)
        return res
