
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        for x in range(length):
            swap = 0
            for y in range(length):
                if y+1 != length and nums[y] > nums[y+1]:
                    temp = nums[y]
                    nums[y] = nums[y+1]
                    nums[y+1] = temp
                    swap = 1
            if swap == 0:
                break