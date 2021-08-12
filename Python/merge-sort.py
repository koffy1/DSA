class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums)
        return nums
        
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return 
        
        midPoint = len(nums) // 2
        leftArray = nums[:midPoint]
        rightArray = nums[midPoint:]
        
        self.mergeSort(leftArray)
        self.mergeSort(rightArray)
        
        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                nums[k] = leftArray[i]
                i += 1
            else:
                nums[k] = rightArray[j]
                j += 1
            k += 1
            
        while i < len(leftArray):
            nums[k] = leftArray[i]
            i += 1
            k += 1
                
        while j < len(rightArray):
            nums[k] = rightArray[j]
            j += 1
            k += 1
                
                
        
        