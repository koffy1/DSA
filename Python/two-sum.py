class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            j = target - nums[i]
            searchArray = nums[i+1:]
            for k in range(len(searchArray)):
                if j == searchArray[k]:
                    return [i, k+i+1]
        