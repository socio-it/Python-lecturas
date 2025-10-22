#Usos de quick sort
import random
author = [3,2 , 0, 1, 4,5,6,7]

def comparar(x, init, end):
    j = init
    for i in range(init+1, end):
        if x[i] < x[init]:
            j+= 1
            x[i], x[j] = x[j], x[i]
    x[init], x[j] = x[j], x[init]
    return j

def sort(x):
    pivot = 0
    return sort_iter(x, 0, len(x), pivot)

def sort_iter(x, init, end, current_total_comparisons):
    m = end - init

    if m <= 1:
        return current_total_comparisons
    comparisons_this_level = m - 1
    updated_total_comparisons = current_total_comparisons + comparisons_this_level
    pivot_index = comparar(x, init, end)
    count_after_left_call = sort_iter(x, init, pivot_index, updated_total_comparisons)
    final_total_comparisons = sort_iter(x, pivot_index + 1, end, count_after_left_call)
    return final_total_comparisons

with open('Coursera3.txt', 'r', encoding='utf-8') as file:
    l = [int(num) for num in file.read().split()]

print(sort(author))
print(author)
print(sort(l))

author = [3,2 , 0, 1, 4,5,6,7]
with open('Coursera3.txt', 'r', encoding='utf-8') as file:
    l = [int(num) for num in file.read().split()]

def sort_iter(x, init, end, current_total_comparisons):
    m = end - init

    if m <= 1:
        return current_total_comparisons
    comparisons_this_level = m - 1
    updated_total_comparisons = current_total_comparisons + comparisons_this_level
    x[init], x[end-1] =x[end-1], x[init]
    pivot_index = comparar(x, init, end)
    count_after_left_call = sort_iter(x, init, pivot_index, updated_total_comparisons)
    final_total_comparisons = sort_iter(x, pivot_index + 1, end, count_after_left_call)
    return final_total_comparisons

print(sort(author))
print(author)
print(sort(l))


author = [3,2 , 0, 1, 4,5,6,7]
with open('Coursera3.txt', 'r', encoding='utf-8') as file:
    l = [int(num) for num in file.read().split()]

def sort_iter(x, init, end, current_total_comparisons):
    m = end - init

    if m <= 1:
        return current_total_comparisons

    first_idx = init
    last_idx = end - 1
    middle_idx = init + (m - 1) // 2

    first_val = x[first_idx]
    middle_val = x[middle_idx]
    last_val = x[last_idx]

    if (first_val < middle_val < last_val) or (last_val < middle_val < first_val):
        median_idx = middle_idx
    elif (middle_val < first_val < last_val) or (last_val < first_val < middle_val):
        median_idx = first_idx
    else:
        median_idx = last_idx

    x[init], x[median_idx] = x[median_idx], x[init]

    comparisons_this_level = m - 1
    updated_total_comparisons = current_total_comparisons + comparisons_this_level

    pivot_index = comparar(x, init, end)

    count_after_left_call = sort_iter(x, init, pivot_index, updated_total_comparisons)

    final_total_comparisons = sort_iter(x, pivot_index + 1, end, count_after_left_call)

    return final_total_comparisons

print(sort(author))
print(author)
print(sort(l))