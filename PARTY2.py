# cook your dish here
t=int(input())
for i in range(0,t):
    n,x,k=map(int,input().split())
    a=n*x
    if k>=a:
        print("YES")
    else:
        print("NO")