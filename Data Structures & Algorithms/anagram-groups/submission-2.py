class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            if "".join(sorted(s)) in h:
                h["".join(sorted(s))].append(s)
            else:
                h["".join(sorted(s))] = [s]
        return list(h.values())