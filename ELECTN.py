# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        if l[i]>=x:
            c=c+1
        else:
            pass
    print(c)