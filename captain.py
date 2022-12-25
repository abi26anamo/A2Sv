k = int(input())
toursts =  input().split()
n = len(toursts)
dic = {}
for tourst in toursts:
    if tourst in dic:
        dic[tourst]+=1
    else:
        dic[tourst]=1
for num in dic:
    if dic[num]==1:
        captain = num
print(captain)
        
