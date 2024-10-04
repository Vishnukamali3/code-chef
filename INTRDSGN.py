# cook your dish here
t=int(input())
for i in range(0,t):
    x1,y1,x2,y2=map(int,input().split())
    a=x1+y1
    b=x2+y2
    if a>b:
        print(b)
    else:
        print(a)