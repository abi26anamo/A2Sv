n = int(input())
edges = 0
graph = []
for _ in range(n):
    row = [int(i)  for i in input().split()]
    graph.append(row)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            edges+=1
print(edges//2)
