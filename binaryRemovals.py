t = int(input())
while t:
    s= input()
    n = len(s)-1
    one =0
    zero =0
    j =0
    for i in range(1,n+1):
        if s[i]==s[i-1] and s[i]=='1' and j==0:
            one =1
            j=1
        if j==1 and s[i]==s[i-1] and s[i]=='0':
            zero =1
    if one ==1 and zero ==1:
        print('No')
    else:
        print('yes')
    t-=1
