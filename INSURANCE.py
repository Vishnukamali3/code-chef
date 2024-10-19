# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    t-=1
    if y<=x:
        print(y)
    else:
        print(x)