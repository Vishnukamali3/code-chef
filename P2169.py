# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    x=[]
    s=input().strip()
    for j in range(N):
        if s[j]=='0':
            x.append('1')
        else:
            x.append('0')
    print(''.join(x))