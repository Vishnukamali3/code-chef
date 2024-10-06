# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    a=x*3
    b=y*2
    if a>b:
        print(b)
    else:
        print(a)