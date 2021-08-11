class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        medianLength = (len(nums1) + len(nums2)) // 2
        mergedArray = []
        counter = 0
        index1 = 0
        index2 = 0
        while counter < medianLength + 1:
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] <= nums2[index2]:
                    mergedArray.append(nums1[index1])
                    index1 += 1
                else:
                    mergedArray.append(nums2[index2])
                    index2 += 1
            elif index1 >= len(nums1):
                mergedArray.append(nums2[index2])
                index2 += 1
            else:
                mergedArray.append(nums1[index1])
                index1 += 1
            counter += 1
            
        print(mergedArray)
        print(medianLength)
        
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 == 0:
            return (mergedArray[-1] + mergedArray[-2]) / 2
        else:
            return mergedArray[-1]
            