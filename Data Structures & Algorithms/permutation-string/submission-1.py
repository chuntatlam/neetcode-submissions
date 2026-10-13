class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding fixed window
        if len(s1) > len(s2):
            return False
        
        freqMap1 = [0] * 26
        for c in s1:
            freqMap1[ord(c) - ord('a')] += 1

        l, r = 0, len(s1) - 1
        freqMap2 = [0] * 26
        for i in range(len(s1) - 1):
            freqMap2[ord(s2[i]) - ord('a')] += 1 # 2. hence, when initialising the sliding window, the right-most int in the window was left out

        while r < len(s2):
            freqMap2[ord(s2[r]) - ord('a')] += 1 # 1. previously this was after r += 1 in the while loop, but r when out of range, so moved the increment of the right-most int of the window to the start of the while loop
            if freqMap1 == freqMap2:
                return True
            freqMap2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
        
        return False
