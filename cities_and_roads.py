n = int(input())
edges = set()
graph = []
for _ in range(n):
    row = [int(i)  for i in input().split()]
    graph.append(row)
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and (i,j) not in edges and  (j,i) not in edges:
            edges.add((i,j))
print(len(edges))
