import sys

n = int(input())
a = [int(i) for i in input().strip().split(' ')]
swaps = 0

for i in range(n):
    currentSwaps = 0

    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            currentSwaps += 1
            
    swaps += currentSwaps
            
    if currentSwaps == 0:
        break
        
print("Array is sorted in " + str(swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
