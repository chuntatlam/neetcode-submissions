class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for i in range(len(nums)):
            if nums[i] in unique_nums:
                return True
            else:
                unique_nums.add(nums[i])
        return False