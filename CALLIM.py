# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    N=list(map(int,input().split()))
    c,s=0,0
    for i in N:
        s=s+i
        if s>k:
            break
        c=c+1
    print(c)
        