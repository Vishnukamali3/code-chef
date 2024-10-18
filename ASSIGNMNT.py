# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a=x*y
    if a<=1440*z:
        print("YES")
    else:
        print("NO")