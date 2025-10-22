#la ventaja de ordenar asi es que el espacio es O(n)
#este algoritmo fue creado por Hoare Circa 1961 QuickSort
from random import random
def quick_sort(a, l, h):
    if l < h:
        p = partition(a, l, h)
        quick_sort(a, l, p-1)
        quick_sort(a, p+1, h)


def partition(a, l, h):
    p = h
    firsthigs = l -1
    for j in range(l,h):
        if a[j] < a[p]:
            a[j], a[firsthigs] = a[firsthigs], a[j]
            firsthigs += 1
    a[p], a[firsthigs] = a[firsthigs], a[p]
    return firsthigs + 1


a = [4,5,7,2,1]
quick_sort(a, 1, len(a)-1)
print(a)