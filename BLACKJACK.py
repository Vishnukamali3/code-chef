# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x+y
    b=21-a
    if b>=1 and b<=10:
        print(b)
    else:
        print("-1")