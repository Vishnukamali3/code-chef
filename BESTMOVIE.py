# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    min_cost=float('inf')
    for i in range(N):
        a,b=list(map(int,input().split()))
        if a>=7:
            min_cost=min(min_cost,b)
    if min_cost==float('inf'):
        print("-1")
    else:
        print(min_cost)