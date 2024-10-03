# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    if x>y:
        a=x
    else:
        a=y
    b=7-a
    print(b)