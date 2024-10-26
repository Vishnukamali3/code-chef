# cook your dish here
t=int(input())
for i in range(t):
    x,y,d=map(int,input().split())
    diff=abs(x-y)
    if diff<=d:
        print("YES")
    else:
        print("NO")