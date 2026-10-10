class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            s = 0
            e = len(nums) - 1
            target = nums[i] * -1
            while s < e:
                if s == i:
                    s += 1
                    continue
                if e == i:
                    e -= 1
                    continue
                if nums[s] + nums[e] == target:
                    triplet = sorted([nums[i], nums[s], nums[e]])
                    res.add(tuple(triplet))
                    s += 1 # need to advance s or move e back to search for other possible answers, cannot use break here
                elif nums[s] + nums[e] > target:
                    e -= 1
                else:
                    s += 1
            
        # res = ((nums[i], nums[j], nums[k]), ...) 
        res_list = list(res)
        res_list = [list(x) for x in res_list]
        return res_list
            
        

            