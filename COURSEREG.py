# cook your dish here
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    a=m-k
    if n<=a:
        print("YES")
    else:
        print("NO")