t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    sign = arr[0]//abs(arr[0])
    curr = arr[0]
    max_sum = 0

    for i in range(n):
        if arr[i]//abs(arr[i]) == sign:
            curr = max(curr, arr[i])
        else:
            max_sum += curr
            sign = arr[i]//abs(arr[i])
            curr = arr[i]
    max_sum +=curr
    print(max_sum)
