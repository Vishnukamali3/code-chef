# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    S=list(map(int,input().split()))
    N=list(map(int,input().split()))
    c=0
    for i in range(n):
        if S[i]==N[i]:
            c=c+1
    print(c)