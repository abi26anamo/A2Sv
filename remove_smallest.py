t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    i=0
    j=n-1
    greater_than_one = False
    for i in range(n-1):
        if arr[i+1]-arr[i]>1:
            greater_than_one=True
            break
    
   
    if not greater_than_one:
        print("YES")
    else:
        print("NO")
 
