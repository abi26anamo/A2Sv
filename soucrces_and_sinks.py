from collections import defaultdict
graph = []
n = int(input())
in_degree = defaultdict(int)
outdegree = defaultdict(int)
for i in range(n):
    row = [int(i) for i in input().split()]
    graph.append(row)        
sinks =[]
sink_count =0
source_count =0
sources= []
for row in range(n):
    for col in range(n):
        if graph[row][col]==1:
            in_degree[col+1]+=1
            outdegree[row+1]+=1
for i in range(1,n+1):
    if outdegree[i]==0 and in_degree[i]!=0:
        sinks.append(i)
        sink_count+=1
    elif outdegree[i]!=0 and in_degree[i]==0:
        sources.append(i)
        source_count+=1
    elif in_degree[i]==0 and outdegree[i]==0:
        sinks.append(i)
        sink_count+=1
        sources.append(i)
        source_count+=1
print(source_count,*sources)
print(sink_count,*sinks)
