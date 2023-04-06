from collections import defaultdict
n = int(input())
adjecency_matrix = []
adjecency_list = defaultdict(list)
for _ in range(n):
    row = [int(j) for j in input().split()]
    adjecency_matrix.append(row)

for row in  range(len(adjecency_matrix)):
    for col in range(len(adjecency_matrix[0])):
        if adjecency_matrix[row][col]==1:
            adjecency_list[row+1].append(col+1)
    print(len(adjecency_list[row+1]),*adjecency_list[row+1])
