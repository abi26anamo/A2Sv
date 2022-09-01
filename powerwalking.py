from collections import defaultdict
t= int(input())
while t:
    n= int(input())
    powers =[int(x) for x in input().split()]
    dic = defaultdict(int)

    for i in range(n):
        dic[powers[i]]+=1
    for i in range(1,n+1):
        print(max(i,len(dic)),end=" ")
    print()
    t-=1
