# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    ak=x*15
    rk=y*2
    if ak>=rk:
        print("YES")
    else:
        print("NO")