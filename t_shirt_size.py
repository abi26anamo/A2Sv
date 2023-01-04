test_cases = int(input())
for _ in range(test_cases):
    a,b  = input().split(" ")
 
    if a[-1]<b[-1]:
        print('>')
    elif a[-1]>b[-1]:
        print('<')
    elif len(a)!=len(b) and a[-1]==b[-1] and a[-1]=='S':
        if len(a)>len(b):
            print('<')
        else:
            print('>')
    elif len(a)!=len(b) and a[-1]==b[-1] and a[-1]=='L':
        if len(a)>len(b):
            print('>')
        else:
            print('<')
    elif len(a)==len(b) and a[-1]==b[-1]:
        print('=')
        
