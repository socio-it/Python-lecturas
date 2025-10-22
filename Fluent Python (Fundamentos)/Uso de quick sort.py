#Usos de quick sort
import random
author = [3,2 , 0, 1, 4,5,6,7]

def find(x):
    sort(x)
    pivot = x[0]
    for i in range(1,len(x)):
        if i+1 > pivot:
            return pivot
        else:
            pivot = x[i]

def comparar(x, init, end):
    j = init
    for i in range(init+1, end):
        if x[i] > x[init]:
            j+= 1
            x[i], x[j] = x[j], x[i]
    x[init], x[j] = x[j], x[init]
    return j

def sort(x):
    return sort_iter(x, 0, len(x))

def sort_iter(x, init, end):
    if init < end:
        j= comparar(x, init, end)
        sort_iter(x,init, j)
        sort_iter(x, j+1, end)
        
print('el pivot es ', find(author))

open 