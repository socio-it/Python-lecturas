
file = 'C:\\Users\\Asus\\Downloads\\task.txt'
numbers =[]
with open(file,'r') as doc:
    for number in doc:
        numbers.append(int(number))

def count_inversions(numbers):
    if len(numbers) <= 1:
        return numbers, 0

    mid = len(numbers) // 2
    left, inv_left = count_inversions(numbers[:mid])
    right, inv_right = count_inversions(numbers[mid:])

    merged, inv_split = merge_and_count(left, right)

    total_inversions = inv_left + inv_right + inv_split
    return merged, total_inversions

def merge_and_count(left, right):
    merged = []
    i = j = inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, inv_count
lis = [1,3,2,5,6]
value = 0
print(count_inversions(numbers))