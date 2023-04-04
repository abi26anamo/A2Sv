t = int(input())

for _ in range(t):
    x = int(input())
    if x%2:
        if x >1:
            print(1)
        else:
            print(3)
    else:
        if (x&(x-1)):
            print(x&~(x-1))
        else:
            print(x+1)
