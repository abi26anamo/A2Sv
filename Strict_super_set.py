A  = set(input().split())
n = int(input())
nsets = [set(input().split()) for _ in range(n)]

isSuper = True
for oneset in nsets:
    if len(oneset)>len(A):
        isSuper = False
        break
    elif A.intersection(oneset)!=oneset:
        isSuper = False
        break
print(isSuper)
