class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        l = list(h.items()) # list of tuples to represent dict
        # e.g. l = [(1,2), (2,1), ... ] where first int is key, second is value
        l.sort(key=lambda x: x[1], reverse=True)
        res = []
        for j in range(k):
            res.append(l[j][0])
        return res