# cook your dish here
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if k*m>=n:
        print("YES")
    else:
        print("NO")