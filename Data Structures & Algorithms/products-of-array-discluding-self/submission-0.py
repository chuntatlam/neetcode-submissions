class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            preffix_prod[i] = preffix_prod[i-1] * nums[i-1]

        for j in range(len(nums) - 2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j+1]

        res = []
        for k in range(len(nums)):
            res.append(preffix_prod[k] * suffix_prod[k])
        
        return res