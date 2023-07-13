from collections import defaultdict
n, m = (int(i) for i in input().split())
arr = []
for _ in range(n):
    arr.append(input())


row_count  = defaultdict(int)
col_count = defaultdict(int)

for r in range(n):
    for c in range(m):
        row_count[(r, arr[r][c])] += 1
        col_count[(c, arr[r][c])] += 1

res = []
for r in range(n):
    for c in range(m):
        if row_count[(r, arr[r][c])] == 1 and col_count[(c, arr[r][c])] == 1:
            res.append((arr[r][c]))
print("".join(res))
