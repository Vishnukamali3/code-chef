# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    if y>x:
        print(y-x)