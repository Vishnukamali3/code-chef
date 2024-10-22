# cook your dish here
t=int(input())
while t>0:
    x,y,m=map(int,input().split())
    t-=1
    a=x*m
    if a<y:
        print("yes")
    else:
        print("no")