from collections import defaultdict
n = int(input())
k = int(input())
adjencents  = defaultdict(list)
for _ in range(k):
     row = [int(i) for i in input().split()]
     if len(row)==3:
          adjencents[row[1]].append(row[2])
          adjencents[row[2]].append(row[1])
     else:
          print(*adjencents[row[1]])
