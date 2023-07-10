n = int(input())
arr = [int(i) for i in input().split()]

even  = False
odd  = False

for num in arr:
    if num % 2 == 0:
        even = True
    else:
        odd = True
if even and odd:
    arr.sort()
print(*arr)
