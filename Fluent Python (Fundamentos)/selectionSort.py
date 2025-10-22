def selectionSort(arr):
    sort = list(arr)
    for i in range(len(sort)):
        indexMin= i
        for j in range(i,len(sort)):
            if  sort[j] < sort[indexMin]:
                indexMin = j
        sort[i],sort[indexMin]= sort[indexMin], sort[i]
    return sort


a=[1,2,3,4,5,9,6,7,5,3,3]
print(selectionSort(a))