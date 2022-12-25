T = int(input())
while T:
    bottom_cub = float("inf")
    n = int(input())
    sideLength = [int(i) for i in input().split()]
    l,r = 0,n-1
    possible = True
    while l <=r:
        if sideLength[r] >= sideLength[l]:
            curr = sideLength[r]
            if curr > bottom_cub:
                possible = False
                break
            else:
                bottom_cub = curr
                r -=1
        elif sideLength[l] > sideLength[r]:
            curr = sideLength[l]
            if curr > bottom_cub:
                possible = False
                break
            else:
                bottom_cub = curr
                l +=1
    if possible:
        print("Yes")  
    else:
        print("No")
    T-=1
