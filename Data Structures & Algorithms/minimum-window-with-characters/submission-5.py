class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = collections.Counter(t)
        missing = len(t)

        best_len = float("inf")
        best_l = 0
        l = 0
        for r, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
