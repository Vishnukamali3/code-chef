# cook your dish here
t=int(input())
for i in range(0,t):
    n,x,y=map(int,input().split())
    a=x+y*2
    if n>=a:
        print("YES")
    elif n<a:
        print("NO")