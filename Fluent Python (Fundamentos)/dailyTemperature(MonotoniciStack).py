def daily_temperature(arr):
    n = len(arr)
    ans = [0] *n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            ans[index] = i - index
        stack.append(i)

    return ans

b = [1,2,3,5,2,3,6]
print(daily_temperature(b))