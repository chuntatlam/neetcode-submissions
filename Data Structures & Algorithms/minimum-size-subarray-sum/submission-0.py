class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        curr_len = 0
        res = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_len = r - l + 1
                if res == 0:
                    res = curr_len
                res = min(res, curr_len)
                curr_sum -= nums[l]
                l += 1
        return res
