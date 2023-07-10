from collections import Counter
n, k = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
arr.sort()

if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(arr[-1])
elif k < n and arr[k - 1] != arr[k]:
    print(arr[k ]-1)
else:
    print(-1)
