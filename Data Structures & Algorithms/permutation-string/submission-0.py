class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        h1 = [0] * 26
        for s in s1:
            h1[ord(s) - ord("a")] += 1
        
        h2 = [0] * 26
        for i in range(len(s1)):
            h2[ord(s2[i]) - ord("a")] += 1
        
        if h1 == h2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            h2[ord(s2[r]) - ord("a")] += 1
            h2[ord(s2[l]) - ord("a")] -= 1
            l += 1
            print(f'h1: {h1}')
            print(f'h2: {h2}')
            if h1 == h2:
                return True
        
        return False

