t = int(input())
for _ in range(t):
    a,b =  (int(i) for i in input().split())
    min_of_both = a if a <b else b
    sum_of_both = a+b
    ans = 0
    left,right = 0,min_of_both
    while left <=right:
        mid = left+(right-left)//2
        if mid*4<=sum_of_both and mid <=min_of_both:
            ans = mid
            left = mid+1
        else:
            right  = mid-1
    print(ans)
        
