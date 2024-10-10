# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=n/2
    if a<=x:
        print("YES")
    else:
        print("NO")