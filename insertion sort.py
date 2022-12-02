def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
arr = [88,21,150,12,66,142,33,111,159,1]
print("the unsorted array :", arr, end="\n")
insertionSort(arr)
print("the sorted array :",arr)
