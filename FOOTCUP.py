# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    if x==0 and y==0:
        print("NO")
    elif x==y:
        print("YES")
    else:
        print("NO")