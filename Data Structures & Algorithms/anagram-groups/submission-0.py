class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            # sort s and use as key in hashmap
            sorted_s = "".join(sorted(s))
            if sorted_s in h:
                h[sorted_s].append(s)
            else:
                h.setdefault(sorted_s, [s])
        return list(h.values())
