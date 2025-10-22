def insertionSort (arr):
    sort = list(arr)
    for i in range(len(sort)):
        j = i
        while j>0 and sort[j] < sort[j -1]:
            sort[j],sort[j-1] = sort[j-1],sort[j]
            j = j-1
    return sort

a=[1,2,3,9,8,7,6]
print(insertionSort(a))