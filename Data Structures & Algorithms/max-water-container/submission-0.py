class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # greedy approach
        max_vol = 0
        s = 0
        e = len(heights) - 1
        while s < e:
            curr_vol = (e - s) * min(heights[s], heights[e])
            max_vol = max(max_vol, curr_vol)
            # compare to check whether to move s or e
            if (min(heights[s+1], heights[e]) > min(heights[s], heights[e-1])):
                s += 1
            else:
                e -= 1
        
        return max_vol
        
