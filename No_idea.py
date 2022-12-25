n,m = [int(i) for i in input().split()]
arr =  input().split()
A = input().split()
B = input().split()
setA = set()
setB = set()
happiness =0
for num in A:
    setA.add(num)
for num in B:
    setB.add(num)

for i in range(n):
    if arr[i] in setA:
        happiness+=1
    elif arr[i] in setB:
        happiness-=1
print(happiness)
