class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        res = collections.defaultdict(list)
        for s in strs:
            freqMap = [0] * 26
            for c in s:
                freqMap[ord(c) - ord("a")] += 1
            freqMap = tuple(freqMap)
            res[freqMap].append(s)
        ans = [list(x) for x in res.values()]
        return ans
