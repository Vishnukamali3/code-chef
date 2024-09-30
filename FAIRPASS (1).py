# cook your dish here
t=int(input())
for i in range(0,t):
    x,n=map(int,input().split())
    if x<n:
        print("YES")
    else:
        print("NO")