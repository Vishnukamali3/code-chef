# cook your dish here
t=int(input())
for i in range(t):
    x,y,r=map(int,input().split())
    a=r//30
    b=x+a
    if b%y==0:
        print(b//y)
    else:
        print((b//y)+1)