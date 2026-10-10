class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        res = 0
        while s < e:
            v = (e - s) * min(heights[s], heights[e])
            res = max(v, res)
            if s < e:
                s += 1
            else:
                e -= 1
        return res
