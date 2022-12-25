n = int(input())
s = [input() for _ in range(n)]
dic ={}
for w in s:
    if w in dic:
        dic[w]+=1
    else:
        dic[w]=1

print(len(dic))
for w in dic:
    print(dic[w], end = ' ')
