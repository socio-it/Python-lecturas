#Skiena - the algorithm manual 
#1-31   
def nearestNeigbor(arr):
    solve = list(arr)
    for i in range(1,len(solve)):
        j = i
        while j > 1 and abs(solve[j]) < abs(solve[j-1]):
            solve[j],solve[j-1] = solve[j-1],solve[j]
            j = j-1
    return solve

def closestPair(arr):
    solve = list(arr)
    for i in range(len(solve)):
        j = i
        while j > 0 and solve[j]<solve[j-1]:
            solve[j],solve[j-1] = solve[j-1],solve[j]
            j = j - 1
    return solve

a = {-21,-5,-1,0,1,3,11}
print(nearestNeigbor(a))
print(closestPair(a))

