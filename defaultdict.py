from collections import defaultdict
n,m =(int(i) for i in input().split())

d = defaultdict(list)

for i in range(1,n+1):
    d[input()].append(str(i))
for j in range(m):
    curr = input()
    if d[curr]:
        print(' '.join(d[curr]))
    else:
        print(-1)
