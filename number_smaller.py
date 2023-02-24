n,m =[int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]


first = 0
res = []
count = 0

for second in range(m):
    while first <n and b[second]>a[first]:
        count+=1
        first+=1
    res.append(count)
print(*res)
