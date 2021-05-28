def quickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    lesser = [i for i in array[1:] if i < pivot]
    greater = [j for j in array[1:] if j >= pivot]
    return quickSort(lesser) + [pivot] + quickSort(greater)
    
print(quickSort([3,1,8,4,9,5,4,2]))