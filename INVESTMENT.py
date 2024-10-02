# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    a=2*y
    if x>=a:
        print("YES")
    else:
        print("NO")