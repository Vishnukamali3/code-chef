# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    x=a+c
    y=b+d
    if x==180 and y==180:
        print("YES")
    else:
        print("NO")