# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=y*30
    if a<=x:
        print("YES")
    else:
        print("NO")