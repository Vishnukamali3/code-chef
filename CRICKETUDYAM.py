# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n>m:
        print("YES")
    else:
        print("NO")