# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    a=list(map(int,input().split()))
    x=[1]
    max_score=a[0]
    for i in range(1,N):
        if a[i]>max_score:
            x.append(1)
            max_score=a[i]
        else:
            x.append(0)
    print(*x)
        