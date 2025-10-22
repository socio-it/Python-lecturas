def binarySearch(arr, item):
    high = len(arr) -1
    low = 0
    for i in range(len(arr)):
        avrg = (high - low) // 2
        value = arr[avrg]

        if(value > item):
            high = avrg -1 
        elif(value < item):
            low = avrg +1
        else:
            return avrg
    
    return -1


a = [1,2,3,4,5,6,7,8]
print(binarySearch(a,4))
print(binarySearch(a,9))
print(binarySearch(a,0))
print(binarySearch(a,1))