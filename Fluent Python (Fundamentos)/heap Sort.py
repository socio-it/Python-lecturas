# heapsort: su mayor ventaja es que a diferencia de marge sort esta
#usa solo O(n) memoria. aunque es mas lenta que quick sort

import heapq

def heap_sort(a):
    return [heapq.heappop(a) for x in range(len(a))]       


a = [1,4,6,23,47,2]
print(heap_sort(a))